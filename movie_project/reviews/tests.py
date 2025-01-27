from django.test import TestCase
from .models import Movie, Review

class reviewTest(TestCase):
    def test_flow(self):
        # (Clean) 변수명 모호, 주석 부족
        mv = Movie.objects.create(title="Test Movie", released_at="2021-01-01", genre="Drama")
        Review.objects.create(movie=mv, content="Great!", score=9)
        Review.objects.create(movie=mv, content="Not bad", score=7)

        # (Optimize) select_related 사용
        reviews = Review.objects.select_related('movie').filter(movie=mv)
        self.assertEqual(reviews.count(), 2)
        # (Clean) 추가 시나리오(수정, 삭제)에 대한 테스트 없음
