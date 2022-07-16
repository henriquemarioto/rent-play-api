from rent_accounts.models import RentAccount
from rest_framework import serializers

from users.models import User

from .models import RentHistory


class RentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentAccount
        exclude = ["login", "password"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "nickname", "first_name", "last_name", "cellphone", "email"]


class RentHistorySerializer(serializers.ModelSerializer):
    rent_account = RentAccountSerializer(read_only=True)
    renter = UserSerializer(read_only=True)

    class Meta:
        model = RentHistory
        fields = "__all__"

        read_only_fields = ["start_date"]
