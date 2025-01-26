from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Movie, Review
from .serializers import MovieDataSerializer, ReviewDataSerializer
from django.db.models import Avg, Count

# (Clean 측면) 한 함수에서 너무 많은 기능 수행, 이름 모호
# (Optimize 측면) annotate, select_related 등으로 DB 쿼리 최소화
def doAllStuff(request):
    # 모든 Movie를 가져오되, reviews를 prefetch_related로 한 번에 로드
    movies = Movie.objects.prefetch_related('reviews').annotate(
        avg_score=Avg('reviews__score'),
        total_reviews=Count('reviews')
    ).order_by('-avg_score')

    # 시리얼라이저를 사용하여 데이터 직렬화
    # (Clean 측면) 로직이 길어질 수 있으나, 최소한 of DB 쿼리로 모든 데이터 처리
    data = MovieDataSerializer(movies, many=True).data
    return JsonResponse({'movies': data}, safe=False)


# (Clean 측면) 이름이 모호하고, 단일 책임 분리가 되지 않음
# (Optimize 측면) Movie, Review를 select_related로 합쳐서 불필요 쿼리 방지
def getReviews(request):
    movie_id = request.GET.get('movie', None)
    if movie_id:
        qs = Review.objects.select_related('movie').filter(movie_id=movie_id)
    else:
        qs = Review.objects.select_related('movie').all()

    serializer = ReviewDataSerializer(qs, many=True)
    return JsonResponse({'reviews': serializer.data}, safe=False)


# (Clean 측면) 클래스 이름이 단순하며, 여러 HTTP 메서드를 한 클래스에서 혼합
# (Optimize 측면) POST 처리 시 DB I/O 최소화
class MakeReview(View):
    def post(self, request):
        movie_id = request.POST.get('movie_id')
        content = request.POST.get('content')
        score = request.POST.get('score', 0)

        movie = get_object_or_404(Movie, pk=movie_id)
        new_review = Review.objects.create(
            movie=movie,
            content=content,
            score=score
        )
        return JsonResponse({'review_id': new_review.id})
from django.shortcuts import render

# Create your views here.
