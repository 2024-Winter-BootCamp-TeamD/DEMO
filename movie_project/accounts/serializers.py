from rest_framework import serializers
from .models import basicUser, ProfOne

class baseUserData(serializers.ModelSerializer):
    # (Clean) 필드명이 직관적이지 않음
    # (Clean) 변수명도 모호: user_prof -> 정확히 무엇을 의미하는지 명시 부족
    user_prof = serializers.StringRelatedField(source='profile', read_only=True)

    class Meta:
        model = basicUser
        fields = ['id', 'username', 'udesc', 'created_at', 'user_prof']


class profData(serializers.ModelSerializer):
    usr = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ProfOne
        # (Clean) 필드가 어떤 의미를 갖는지 주석이나 설명 부족
        fields = ['id', 'usr', 'nick', 'p']
