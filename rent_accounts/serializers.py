from games.models import Game
from games.serializers import GameSerializer
from platforms.models import Platform
from rest_framework import serializers
from users.models import User
from users.serializers import UserSerializer

from .models import RentAccount


class PlatformChoices(serializers.ChoiceField):
    platforms = Platform.objects.all()
    platform_choices = [platform.name for platform in platforms]


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]


class CreateRentAccountSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True)
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = RentAccount
        fields = [
            "id",
            "login",
            "password",
            "price_per_day",
            "owner",
            "games",
        ]
        extra_kwargs = {
            "login": {"write_only": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data: dict):
        games = validated_data.pop("games")

        rent_account = RentAccount.objects.create(**validated_data)

        for game in games:
            jogo, _ = Game.objects.get_or_create(**game)
            rent_account.games.add(jogo)

        return rent_account


class ListAndRetriveRentAccountSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = RentAccount
        exclude = ["login", "password"]
        depth = 1


class UpdateDeleteRentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentAccount
        exclude = ["owner", "platform", "renter", "games"]
