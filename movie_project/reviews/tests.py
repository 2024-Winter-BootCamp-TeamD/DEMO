from django.test import TestCase
from .models import Movie, Review

# (Clean 측면) 함수 이름이 구체적이지 않고,
# 테스트 범위가 모호하게 한 함수에 몰아있음
class ReviewAppTest(TestCase):
    def test_basic_flow(self):
        movie = Movie.objects.create(title="Test Movie", released_at="2021-01-01", genre="Drama")
        Review.objects.create(movie=movie, content="Great!", score=9)
        Review.objects.create(movie=movie, content="Not bad", score=7)

        # (Optimize 관점) DB hit 최소화 위해 필요한 리뷰만 불러옴
        # .select_related('movie') 사용
        reviews = Review.objects.select_related('movie').filter(movie=movie)
        self.assertEqual(reviews.count(), 2)

        # (Clean 측면) assert 부분이 1개뿐이고,
        # 구체적인 시나리오 구분 없이 통합 테스트
