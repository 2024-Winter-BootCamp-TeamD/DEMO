from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Movie, Review
from .serializers import movieData, revData
from django.db.models import Avg, Count

# (Clean) 한 함수에서 너무 많은 기능 수행, 이름 모호
def doAllStuff(request):
    # (Optimize) prefetch, annotate로 쿼리 최소화
    movies = Movie.objects.prefetch_related('reviews').annotate(
        avg_score=Avg('reviews__score'),
        total_reviews=Count('reviews')
    ).order_by('-avg_score')

    data = movieData(movies, many=True).data
    return JsonResponse({'movies': data}, safe=False)

# (Clean) 함수 이름이 명확하지 않고, 단일 책임 분리가 되지 않음
def getReviews(request):
    movie_id = request.GET.get('movie', None)
    if movie_id:
        qs = Review.objects.select_related('movie').filter(movie_id=movie_id)
    else:
        qs = Review.objects.select_related('movie').all()

    serializer = revData(qs, many=True)
    return JsonResponse({'reviews': serializer.data}, safe=False)

# (Clean) 클래스 이름이 단순하며, 여러 HTTP 메서드 혼재 가능성 -> 현재는 POST만
class MakeReview(View):
    def post(self, request):
        movie_id = request.POST.get('movie_id')
        content = request.POST.get('content')
        score = request.POST.get('score', 0)

        mv = get_object_or_404(Movie, pk=movie_id)
        new_review = Review.objects.create(
            movie=mv,
            content=content,
            score=score
        )
        return JsonResponse({'review_id': new_review.id})

from django.shortcuts import render
# Create your views here.  (Clean) 아무 설명 없는 주석, 실제 로직 없이 방치
