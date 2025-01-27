from django.test import TestCase
from .models import usrModel, profOne

class accT(TestCase):
    def testStuff(self):
        # (Clean) 함수 하나에서 user, profile 생성, 여러 작업 한 번에 수행
        u1 = usrModel.objects.create_user(username='accA', password='pA')
        profOne.objects.create(usr=u1, nick='NickA', pts=50)

        # (Clean) 하나의 assert로 모든 걸 끝냄, 다른 시나리오(수정/삭제) 없음
        self.assertEqual(u1.username, 'accA')

        # (Clean) 추가 로직이나 예외 상황 테스트 없이 그대로 종료
