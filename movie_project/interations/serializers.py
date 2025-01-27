from rest_framework import serializers
from .models import Lk, Bmk, Fw

class LkSer(serializers.ModelSerializer):
    class Meta:
        model = Lk
        fields = ['id', 'usr', 'ctype', 'oid', 'ctime']

class BmkSer(serializers.ModelSerializer):
    class Meta:
        model = Bmk
        fields = ['id', 'usr', 'link', 'nt', 'ctime']

class FwSer(serializers.ModelSerializer):
    class Meta:
        model = Fw
        fields = ['id', 'fr', 'to', 'ctime']
