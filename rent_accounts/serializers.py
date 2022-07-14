from games.models import Game
from platforms.serializers import PlatformSerializer
from rest_framework import serializers
from users.models import User
from users.serializers import UserSerializer

from .models import RentAccount


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id"]


class CreateRentAccountSerializer(serializers.ModelSerializer):
    games = GamesSerializer(read_only=True, many=True)
    game_ids = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all(), many=True, source="games", write_only=True
    )
    owner = OwnerSerializer(read_only=True)
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
            "game_ids",
            "platform",
        ]
        extra_kwargs = {
            "login": {"write_only": True},
            "password": {"write_only": True},
        }


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
    games = GamesSerializer(read_only=True, many=True)
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
    games = GamesSerializer(read_only=True, many=True)
    game_ids = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all(), many=True, source="games", write_only=True
    )

    class Meta:
        model = RentAccount
        fields = ["game_ids", "games"]

    def update(self, instance, validated_data):
        instance.games.remove(*validated_data["games"])
        return {""}
