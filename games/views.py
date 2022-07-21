from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import SuperUserPermissions

from .exceptions import GameAlreadyExistsInDataBase, PlatformIsRequired
from .mixins import SerializerByMethodMixin
from .models import Game
from .serializers import GameSerializer


class GameViews(SerializerByMethodMixin, generics.ListCreateAPIView):

    queryset = Game.objects.all()
    serializer_map = {"POST": GameSerializer, "GET": GameSerializer}

    def perform_create(self, serializer):
        game_api_id_data = Game.objects.filter(
            game_api_id=self.request.data["game_api_id"]
        )
        game_name_data = Game.objects.filter(name=self.request.data["name"])

        if not self.request.data.get("platforms"):
            raise PlatformIsRequired

        if game_api_id_data or game_name_data:
            raise GameAlreadyExistsInDataBase

        serializer.save(platforms=self.request.data.get("platforms"))

    def get_queryset(self):
        return Game.objects.all().order_by("-release_date")


class RetrieveUpdateDestroyGameView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, SuperUserPermissions]

    queryset = Game.objects.all()
    serializer_class = GameSerializer
