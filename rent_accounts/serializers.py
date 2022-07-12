from rest_framework import serializers

from .models import Rent_Account


class RentAccauntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent_Account
        fields = ["id", ""]
    
    extra_kwargs = {
        ""
    }