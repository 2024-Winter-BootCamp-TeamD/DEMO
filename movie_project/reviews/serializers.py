from rest_framework import serializers
from .models import Mv, Rv

class MvData(serializers.ModelSerializer):
    rvs_list = serializers.StringRelatedField(many=True, source='rvs')

    class Meta:
        model = Mv
        fields = ['id', 'ttl', 'gnr', 'rdate', 'rvs_list']

class RvData(serializers.ModelSerializer):
    mv_ttl = serializers.CharField(source='mv.ttl', read_only=True)

    class Meta:
        model = Rv
        fields = ['id', 'cont', 'sc', 'ctime', 'mv_ttl']
