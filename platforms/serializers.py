from rest_framework import serializers

from .models import Platform


class CreateListPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"
