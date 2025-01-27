from rest_framework import serializers
from .models import usrModel, profOne

class uData(serializers.ModelSerializer):
    prof_data = serializers.StringRelatedField(source='prof', read_only=True)

    class Meta:
        model = usrModel
        fields = ['id', 'username', 'bioinfo', 'ctime', 'prof_data']

class pData(serializers.ModelSerializer):
    usr_name = serializers.CharField(source='usr.username', read_only=True)

    class Meta:
        model = profOne
        fields = ['id', 'usr_name', 'nick', 'pts']
