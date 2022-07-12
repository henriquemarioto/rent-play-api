from games.models import Game
from users.models import User
from games.serializers import GameSerializer
from rest_framework import serializers
from users.serializers import UserSerializer

from .models import RentAccount

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]


class RentAccountCreateSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True)
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = RentAccount
        fields = [
            "id",
            "plataform",
            "login",
            "password",
            "price_per_day",
            "owner",
            "games",
        ]
        extra_kwargs = {"login": {"write_only": True}, "password": {"write_only": True}}


    def create(self, validated_data: dict):
        games = validated_data.pop("games")

        rent_account = RentAccount.objects.create(**validated_data)
        for game in games:
            jogo, _ = Game.objects.get_or_create(**game)
            rent_account.games.add(jogo)

        return rent_account
