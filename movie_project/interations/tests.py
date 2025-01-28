from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Lk, Bmk, Fw

User = get_user_model()

class intT(TestCase):
    def test_inter(self):
        u1 = User.objects.create_user(username='u1', password='p1')
        u2 = User.objects.create_user(username='u2', password='p2')

        # Like
        lk = Lk.objects.create(usr=u1, ctype='post', oid=10)
        # Bookmark
        Bmk.objects.create(usr=u2, link='http://ex.com', nt='Samp')
        # Follow
        Fw.objects.create(fr=u1, to=u2)

        # (Clean) 한 메서드에 다 때려넣음, assert 최소
        self.assertEqual(lk.usr, u1)
