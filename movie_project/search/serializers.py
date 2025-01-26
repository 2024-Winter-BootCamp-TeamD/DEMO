from rest_framework import serializers
from .models import SearchQuery

# (Optimize) 필드 수 최소화로 직렬화 오버헤드 감소
# (Clean) 네이밍이나 목적 설명이 부족
class SearchQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchQuery
        fields = ['id', 'keyword', 'created_at']
