import datetime
from platform import platform

from django.shortcuts import get_object_or_404
from games.models import Game
from games.serializers import GameSerializer
from platforms.models import Platform
from platforms.serializers import PlatformSerializer
from rents_history.models import RentHistory
from rest_framework import serializers
from users.models import User
from users.serializers import UserSerializer

from .models import RentAccount


class CreateRentAccountSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True)
    owner = UserSerializer(read_only=True)
    platform = PlatformSerializer(read_only=True)

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
        rent_account = RentAccount.objects.create(**validated_data)

        for item in games:
            platforms = item.pop("platforms")

            game, _ = Game.objects.get_or_create(**item)

            for platform in platforms:
                platform_data = Platform.objects.get(pk=platform.id)
                game.platforms.add(platform_data)

            rent_account.games.add(game)

        return rent_account

    def update(self, instance, validated_data):
        for item in validated_data["games"]:
            game, _ = Game.objects.get_or_create(**item)
            instance.games.add(game)

        return instance


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
    games = GameSerializer(many=True)

    class Meta:
        model = RentAccount
        fields = ["games"]

    def update(self, instance, validated_data):
        for item in validated_data["games"]:
            game, _ = Game.objects.get_or_create(**item)
            instance.games.add(game)

        return instance


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
        return {}
