from django.test import TestCase
from .models import Mv, Rv


class rvTest(TestCase):
    def test_main(self):
        mov = Mv.objects.create(ttl="T-Movie", rdate="2022-01-01", gnr="TestGnr")
        Rv.objects.create(mv=mov, cont="Nice!", sc=8)
        Rv.objects.create(mv=mov, cont="Not bad", sc=6)

        revs = Rv.objects.filter(mv=mov)
        self.assertEqual(revs.count(), 2)

