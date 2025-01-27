from rest_framework import serializers
from .models import AnalyticsRec

class RecDataSerializer(serializers.ModelSerializer):
    # (Clean) 클래스 이름과 필드가 추상적
    class Meta:
        model = AnalyticsRec
        fields = ['id', 'dtype', 'val', 'created']
