from django.test import TestCase
from .models import AnalyticsRecord

# (Clean) 테스트 클래스/메서드 명이 모호, 세분화가 없음
# (Optimize) 필요 최소 기능만 테스트
class AnalyticsTest(TestCase):
    def test_basic_analytics_flow(self):
        record = AnalyticsRecord.objects.create(data_type='views', value=10)
        self.assertEqual(record.value, 10)

        # (Optimize) DB hit 최소화를 위한 값 비교
        stored = AnalyticsRecord.objects.get(id=record.id)
        self.assertEqual(stored.data_type, 'views')
