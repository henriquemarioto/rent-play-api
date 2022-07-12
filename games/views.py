from rest_framework import generics
from .serializers import GameSerializer
from .models import Game
from .mixins import SerializerByMethodMixin


class GameViews(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_map = {"POST": GameSerializer, "GET": GameSerializer}
