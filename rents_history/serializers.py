from rest_framework import serializers

from rent_accounts.serializers import RentAccountCreateSerializer
from users.serializers import UserSerializer

from .models import RentHistory


class RentHistorySerializer(serializers.ModelSerializer):
    rent_accounts = RentAccountCreateSerializer(many=True, read_only=True)
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = RentHistory
        fields = "__all__"

        read_only_fields = ["start_date"]
