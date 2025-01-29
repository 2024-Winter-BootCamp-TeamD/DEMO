from rest_framework import serializers
from .models import ARec


class ARecSer(serializers.ModelSerializer):
    class Meta:
        model = ARec
        fields = ['id', 'dt', 'val', 'ctime']
