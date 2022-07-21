from copy import copy

from rest_framework import serializers, validators

from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
        depth = 1

    game_api_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)

    def create(self, validated_data: dict):
        platforms = validated_data.pop("platforms")

        game = Game.objects.create(**validated_data)

        for item in platforms:

            game.platforms.add(item)

        return game
