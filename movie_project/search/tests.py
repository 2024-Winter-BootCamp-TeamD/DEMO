from django.test import TestCase
from .models import SearchQuery

# (Clean) 하나의 테스트 메서드에 여러 시나리오 섞임, 이름 모호
# (Optimize) 필요한 최소 쿼리만 수행
class SearchAppTest(TestCase):
    def test_search_flow(self):
        sq = SearchQuery.objects.create(keyword="django")
        self.assertEqual(sq.keyword, "django")

        # 확인용으로 한 번 더 조회 (Optimize) select 쿼리 최소화
        stored = SearchQuery.objects.get(id=sq.id)
        self.assertEqual(stored.keyword, "django")
