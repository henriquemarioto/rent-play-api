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


class AddGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

        read_only_fields = ["platforms"]

    game_api_id = serializers.IntegerField()
    name = serializers.CharField(max_length=16)


class CreateRentAccountSerializer(serializers.ModelSerializer):
    games = AddGameSerializer(many=True)
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
        depth = 1

    def create(self, validated_data: dict):
        
        games = validated_data.pop("games")
        rent_account = RentAccount.objects.create(**validated_data)
        for item in games:
            game_exists = Game.objects.get(game_api_id=item["game_api_id"])
            if not game_exists:
                game = Game.objects.create(**item)
                
                platforms = game.pop("platforms")

                for platform in platforms:
                    game.platforms.add(platform)
                
                rent_account.games.add(game)

            rent_account.games.add(game_exists)

        return rent_account

    def update(self, instance, validated_data):
        for item in validated_data["games"]:
            game, _ = Game.objects.get_or_create(**item)
            instance.games.add(game)

        return instance


class ListAndRetriveRentAccountSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    renter = UserSerializer(read_only=True)

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
        print("AQUIIIIIIIIIIIIIIIIIII", instance.platform.id)
        for item in validated_data["games"]:
            item.pop("platforms")

            game, _ = Game.objects.get_or_create(**item)
            game.platforms.add(instance.platform.id)

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
