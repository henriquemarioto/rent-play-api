from rest_framework import serializers

from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "name", "image", "release_date"]

    def create(self, validated_data: dict):
        return Game.objects.create(**validated_data)
