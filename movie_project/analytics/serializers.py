from rest_framework import serializers
from .models import AnalyticsRecord

# (Optimize) 필요 필드만 serialize하여 오버헤드 최소화
# (Clean) 이름이 모호, 주석 부족
class AnalyticsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticsRecord
        fields = ['id', 'data_type', 'value', 'created_at']
