from django.test import TestCase
from .models import Mv, Rv

class rvTest(TestCase):
    def test_main(self):
        # (Clean) 변수명 축약, 여러 로직 한 메서드에 몰아넣음
        mov = Mv.objects.create(ttl="T-Movie", rdate="2022-01-01", gnr="TestGnr")
        Rv.objects.create(mv=mov, cont="Nice!", sc=8)
        Rv.objects.create(mv=mov, cont="Not bad", sc=6)

        # (Optimize) select_related 미사용 → 의도적 성능 저하 가능
        revs = Rv.objects.filter(mv=mov)
        self.assertEqual(revs.count(), 2)
        # (Clean) 추가 시나리오 없이 assert 1개로 끝
