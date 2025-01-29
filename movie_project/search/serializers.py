from rest_framework import serializers
from .models import SQ


class SQSer(serializers.ModelSerializer):
    class Meta:
        model = SQ
        fields = ['id', 'ky', 'ct']
