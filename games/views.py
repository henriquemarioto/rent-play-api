from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import SuperUserPermissions

from .exceptions import GameAlreadyExistsInDataBase
from .mixins import SerializerByMethodMixin
from .models import Game
from .serializers import GameSerializer


class GameViews(SerializerByMethodMixin, generics.ListCreateAPIView):

    queryset = Game.objects.all()
    serializer_map = {"POST": GameSerializer, "GET": GameSerializer}

    def perform_create(self, serializer):
        game = Game.objects.filter(
            game_api_id=self.request.data["game_api_id"], name=self.request.data["name"]
        )

        if game:
            raise GameAlreadyExistsInDataBase


class RetrieveUpdateDestroyGameView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, SuperUserPermissions]

    queryset = Game.objects.all()
    serializer_class = GameSerializer
