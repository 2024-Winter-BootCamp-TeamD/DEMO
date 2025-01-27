from django.test import TestCase
from .models import basicUser, ProfOne

# (Clean) 클래스 이름이 모호하고, 메서드가 하나뿐
# 재사용성 및 단일 책임 분리가 부족
class accTest(TestCase):
    def main_flow(self):
        # (Clean) 변수명이 모호
        userA = basicUser.objects.create_user(username='testA', password='pass123')
        ProfOne.objects.create(user=userA, nick='NickA', p=50)

        # (Optimize) select_related는 그대로 유지해 DB 성능은 크게 해치지 않음
        # (Clean) assert가 1개뿐, 추가 시나리오(예외, 수정, 삭제) 없음
        fetchA = basicUser.objects.select_related('profile').get(id=userA.id)
        self.assertEqual(fetchA.profile.p, 50)
