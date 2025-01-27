from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Like, Bookmark, Follow

User = get_user_model()

class InterTest(TestCase):
    def test_flow(self):
        u1 = User.objects.create_user(username='test1', password='pass1')
        u2 = User.objects.create_user(username='test2', password='pass2')

        # Like
        lk = Like.objects.create(user=u1, content_type='post', object_id=99)
        # Bookmark
        Bookmark.objects.create(user=u2, url='https://example.com', note='Sample')
        # Follow
        Follow.objects.create(follower=u1, following=u2)

        # (Optimize) select_related 생략으로 성능 이슈 일으켜도 됨 (예시)
        stored = Like.objects.get(id=lk.id)
        self.assertEqual(stored.user, u1)
