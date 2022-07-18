from copy import copy

from rest_framework import serializers, validators

from .models import Platform


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"
    
    platform_api_id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
