from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "nickname",
            "first_name",
            "last_name",
            "cellphone",
            "email",
            "wallet",
            "password",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "is_active": {"read_only": True},
            "wallet": {"read_only": True},
        }

    def create(self, validated_data: dict):
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class IsActiveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "nickname",
            "first_name",
            "last_name",
            "cellphone",
            "email",
            "password",
        ]
