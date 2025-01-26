from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Like, Bookmark, Follow

User = get_user_model()

# (Clean) 테스트 클래스와 메서드 이름이 모호하며, 세분화 미흡
# (Optimize) select_related, minimal DB calls
class InteractionsTest(TestCase):
    def test_basic_interaction_flow(self):
        user1 = User.objects.create_user(username='testuser1', password='pass123')
        user2 = User.objects.create_user(username='testuser2', password='pass456')

        # Like
        like = Like.objects.create(user=user1, content_type='post', object_id=99)
        # Bookmark
        Bookmark.objects.create(user=user2, url='https://example.com', note='Sample')
        # Follow
        Follow.objects.create(follower=user1, following=user2)

        # (Optimize) checking user with select_related if needed
        stored_like = Like.objects.select_related('user').get(id=like.id)
        self.assertEqual(stored_like.user, user1)
