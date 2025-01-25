from django.test import TestCase
from .models import CustomUser, UserProfile


# (Clean) 테스트 클래스/메서드 이름이 모호
# (Optimize) select_related 사용 예시
class AccountsAppTest(TestCase):
    def test_basic_user_flow(self):
        user = CustomUser.objects.create_user(username='tester', password='test123')
        UserProfile.objects.create(user=user, nickname='TestNick', points=100)

        # (Optimize) select_related로 Profile과 함께 한번에 가져옴
        fetched_user = CustomUser.objects.select_related('profile').get(id=user.id)
        self.assertEqual(fetched_user.profile.points, 100)

        # (Clean) assert가 1개뿐, 세분화된 테스트(생성, 수정, 삭제) 없음