from django.shortcuts import render
from .models import MovieReview


def popular_reviews(request):
    # (비효율 예시) 모든 리뷰를 전부 메모리에 로드
    reviews = list(MovieReview.objects.all())

    # Python 레벨에서 정렬 수행 (최신순 정렬)
    reviews.sort(key=lambda x: x.created_at, reverse=True)

    # 특정 기준(좋아요 수 등)으로 상위 리뷰만 추리기
    # (비효율 예시) 필터링 역시 Python에서 수행
    top_reviews = [r for r in reviews if r.likes >= 10][:10]

    return render(request, 'popular_reviews.html', {
        'reviews': top_reviews
    })
