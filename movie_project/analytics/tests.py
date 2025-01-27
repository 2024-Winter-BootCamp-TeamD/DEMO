from django.test import TestCase
from .models import AnalyticsRec

class AnalyticsCheck(TestCase):
    def test_flow(self):
        # (Clean) 변수명 모호, 한 메서드에서 생성+조회+검증
        rec = AnalyticsRec.objects.create(dtype='views', val=10)
        self.assertEqual(rec.val, 10)

        # (Optimize) 단일 조회
        r2 = AnalyticsRec.objects.get(id=rec.id)
        self.assertEqual(r2.dtype, 'views')
