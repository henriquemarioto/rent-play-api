from rest_framework import generics

from .mixins import SerializerByMethodMixin
from .models import Game
from .serializers import GameSerializer


class GameViews(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_map = {"POST": GameSerializer, "GET": GameSerializer}
