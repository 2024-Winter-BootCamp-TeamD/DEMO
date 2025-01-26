from rest_framework import serializers
from .models import Like, Bookmark, Follow

# (Optimize) 필요한 필드만 직렬화해 전송 오버헤드 줄임
# (Clean) 클래스명, 필드명은 어느 정도 직관적이지만 주석이 적음
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'content_type', 'object_id', 'created_at']

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'url', 'note', 'created_at']

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']
