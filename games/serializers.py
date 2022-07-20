from copy import copy
from rest_framework import serializers, validators

from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
    
    game_api_id = serializers.IntegerField()
    name = serializers.CharField(max_length=16)
   
