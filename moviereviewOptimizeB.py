from django.shortcuts import render, get_object_or_404
from .models import MovieReview, Movie


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = MovieReview.objects.filter(movie=movie)

    total_score = 0
    count = 0

    # 리뷰를 순회하며 평점을 더하고 횟수를 계산
    for review in reviews:
        # (비효율 예시) 각 리뷰마다 DB조회가 필요한 로직이 들어간다면, 쿼리가 증가
        total_score += review.score
        count += 1

    avg_score = total_score / count if count > 0 else 0

    # 영화 상세 템플릿으로 전달
    return render(request, 'movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'average_score': avg_score
    })