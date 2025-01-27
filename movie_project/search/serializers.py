from rest_framework import serializers
from .models import SQ

class SQSer(serializers.ModelSerializer):
    # (Clean) 클래스 이름이 짧고 목적 모호, 필드명 설명 부족
    class Meta:
        model = SQ
        fields = ['id', 'ky', 'ct']
