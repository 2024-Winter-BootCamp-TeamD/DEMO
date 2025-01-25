from django.shortcuts import render
from .models import MovieReview

def search_review(request):
    keyword = request.GET.get('q', '')
    all_reviews = MovieReview.objects.all()  # 모든 리뷰를 불러옴

    # (비효율 예시) 파이썬 레벨에서 문자열 검사
    matched_reviews = []
    for review in all_reviews:
        if keyword.lower() in review.content.lower():
            matched_reviews.append(review)

    return render(request, 'search_result.html', {
        'reviews': matched_reviews,
        'keyword': keyword
    })