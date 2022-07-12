import email
from questionary import password
from rest_framework import serializers
from .models import RentAccount


class RentAccauntSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentAccount
        fields = ["id", "plataform", "login", "price_per_day"]

    extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict):
        return RentAccount.objects.create(**validated_data)


class RentAccountLogin(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
