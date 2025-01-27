from rest_framework import serializers
from .models import QueryLog

class QLogSer(serializers.ModelSerializer):
    # (Clean) 클래스명과 목적이 모호, 주석 부재
    class Meta:
        model = QueryLog
        fields = ['id', 'kw', 'ctime']
