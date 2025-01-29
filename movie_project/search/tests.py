from django.test import TestCase
from .models import SQ

class sCheck(TestCase):
    def test_stuff(self):
        obj = SQ.objects.create(ky="TestCase")
        self.assertEqual(obj.ky, "TestCase")

        again = SQ.objects.get(id=obj.id)
        self.assertEqual(again.ky, "TestCase")
