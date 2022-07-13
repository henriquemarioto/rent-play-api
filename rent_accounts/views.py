from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from games.models import Game
from platforms.models import Platform
from users.mixins import SerializerByMethodMixin

from .models import RentAccount
from .serializers import (
    CreateRentAccountSerializer,
    ListAndRetriveRentAccountSerializer,
    UpdateDeleteRentAccountSerializer,
)


class ListCreateRentAccountView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = RentAccount.objects.all()
    serializer_map = {
        "GET": ListAndRetriveRentAccountSerializer,
        "POST": CreateRentAccountSerializer,
    }

    def perform_create(self, serializer):
        platform = get_object_or_404(Platform, pk=self.request.data.get("platform"))
        games = Game.objects.filter(id__in=tuple(self.request.data.get("games")))
        print("AQUIIIIIIIIIIIIIIIIII", games)
        serializer.save(owner=self.request.user, platform=platform, games=games)


class RetrieveUpdateDestroyRentAccountView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    queryset = RentAccount.objects.all()
    serializer_map = {
        "GET": ListAndRetriveRentAccountSerializer,
        "PATCH": UpdateDeleteRentAccountSerializer,
        "DELETE": UpdateDeleteRentAccountSerializer,
    }

