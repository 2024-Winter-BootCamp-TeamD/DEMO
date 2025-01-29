from django.test import TestCase
from .models import usrModel, profOne


class accT(TestCase):
    def testStuff(self):
        u1 = usrModel.objects.create_user(username='accA', password='pA')
        profOne.objects.create(usr=u1, nick='NickA', pts=50)
        self.assertEqual(u1.username, 'accA')


