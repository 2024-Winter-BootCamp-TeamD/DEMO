from django.test import TestCase
from .models import QueryLog

class sTest(TestCase):
    def test_flow(self):
        # (Clean) 한 메서드에 생성+검증 혼합, 별도 시나리오 분리 없음
        qobj = QueryLog.objects.create(kw="DjangoTest")
        self.assertEqual(qobj.kw, "DjangoTest")

        # (Optimize) 직접 접근, 추가 로직이나 주석 없음
        fetched = QueryLog.objects.get(id=qobj.id)
        self.assertEqual(fetched.kw, "DjangoTest")
