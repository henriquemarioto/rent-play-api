from games.models import Game
from games.serializers import GameSerializer
from platforms.models import Platform
from platforms.serializers import PlatformSerializer
from rest_framework import serializers
from users.models import User
from users.serializers import UserSerializer

from .models import RentAccount


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]


class CreateRentAccountSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True)
    owner = OwnerSerializer(read_only=True)
    platform = PlatformSerializer()

    class Meta:
        model = RentAccount
        fields = [
            "id",
            "login",
            "password",
            "price_per_day",
            "owner",
            "games",
            "platform",
        ]
        extra_kwargs = {
            "login": {"write_only": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data: dict):
        games = validated_data.pop("games")
        platform_data = validated_data.pop("platform")

        platform, _ = Platform.objects.get_or_create(**platform_data)
        rent_account = RentAccount.objects.create(**validated_data, platform=platform)

        for item in games:
            game, _ = Game.objects.get_or_create(**item)
            rent_account.games.add(game)

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


class AddGamesRentAccountByIdSerializer(serializers.ModelSerializer):
    games = GameSerializer(read_only=True, many=True)
    game_ids = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all(), many=True, source="games", write_only=True
    )

    class Meta:
        model = RentAccount
        fields = ["game_ids", "games"]

    def update(self, instance, validated_data):
        instance.games.add(*validated_data["games"])
        return validated_data


class RemoveGamesRentAccountByIdSerializer(serializers.ModelSerializer):
    games = GameSerializer(read_only=True, many=True)
    game_ids = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all(), many=True, source="games", write_only=True
    )

    class Meta:
        model = RentAccount
        fields = ["game_ids", "games"]

    def update(self, instance, validated_data):
        instance.games.remove(*validated_data["games"])
        return {""}
