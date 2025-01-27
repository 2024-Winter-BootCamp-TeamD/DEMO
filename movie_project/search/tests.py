from django.test import TestCase
from .models import SQ

class sCheck(TestCase):
    def test_stuff(self):
        # (Clean) 변수명 애매, 주석 없음
        obj = SQ.objects.create(ky="TestCase")
        # 단일 시나리오만 체크, assert 1~2개로 끝
        self.assertEqual(obj.ky, "TestCase")

        # (Optimize) 간단히 한 번 더 조회
        again = SQ.objects.get(id=obj.id)
        self.assertEqual(again.ky, "TestCase")
        # (Clean) 수정/삭제 시나리오 등은 전혀 테스트하지 않음
