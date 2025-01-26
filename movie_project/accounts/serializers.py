from rest_framework import serializers
from .models import CustomUser, UserProfile

# (Optimize) read_only로 불필요한 쓰기 연산 방지
# (Clean) Serializer 이름이 구체적이지 않아 의도가 잘 드러나지 않음
class UserDataSerializer(serializers.ModelSerializer):
    # (Clean) 변수명 모호. user_profile -> profile_data 등 더 명확히 가능.
    user_profile = serializers.StringRelatedField(source='profile', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'bio', 'created_at', 'user_profile']


class UserProfileSerializer(serializers.ModelSerializer):
    user_info = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user_info', 'nickname', 'points']
