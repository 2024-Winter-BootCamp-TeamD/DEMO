from django.test import TestCase
from .models import ARec

class anTest(TestCase):
    def test_basic(self):
        r = ARec.objects.create(dt='typeA', val=10)
        self.assertEqual(r.val, 10)

        got = ARec.objects.get(id=r.id)
        self.assertEqual(got.dt, 'typeA')

