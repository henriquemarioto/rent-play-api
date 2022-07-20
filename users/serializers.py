from lib2to3.pgen2 import token

from rest_framework import serializers

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
            "password",
        ]
        read_only_fields = ["wallet"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_active": {"read_only": True},
        }

    def create(self, validated_data: dict):
        return User.objects.create_user(**validated_data)


class UpdateUserSerializer(serializers.ModelSerializer):
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
        extra_kwargs = {
            "password": {"write_only": True},
            "is_active": {"read_only": True},
        }

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance


class GetUserWithWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname", "first_name", "last_name", "cellphone", "email", "wallet"]

class UpdateUserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname", "first_name", "last_name", "cellphone", "email", "wallet"]
        read_only_fields = ["nickname", "first_name", "last_name", "cellphone", "email"]

    def update(self, instance: User, validated_data: dict):
        instance.wallet += validated_data["wallet"]

        setattr(instance, "wallet", instance.wallet)

        instance.save()

        return instance

class UpdateUserWalletWithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname", "first_name", "last_name", "cellphone", "email", "wallet"]
        read_only_fields = ["nickname", "first_name", "last_name", "cellphone", "email"]

    def update(self, instance: User, validated_data: dict):
        instance.wallet -= validated_data["wallet"]

        setattr(instance, "wallet", instance.wallet)

        instance.save()

        return instance

class UserLoginSerializer(serializers.Serializer):
    token = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    email = serializers.EmailField(write_only=True)
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
            "wallet",
            "is_active"
        ]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def update(self, instance: User, validated_data: dict):
       
        validated_data["wallet"] += instance.wallet

        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
