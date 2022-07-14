from django.shortcuts import get_object_or_404
from platforms.models import Platform
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.mixins import SerializerByMethodMixin

from .models import RentAccount
from .serializers import (
    AddGamesRentAccountByIdSerializer,
    CreateRentAccountSerializer,
    ListAndRetriveRentAccountSerializer,
    RemoveGamesRentAccountByIdSerializer,
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
        serializer.save(owner=self.request.user, platform=platform)


class RetrieveUpdateDestroyRentAccountView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    queryset = RentAccount.objects.all()
    serializer_map = {
        "GET": ListAndRetriveRentAccountSerializer,
        "PATCH": UpdateDeleteRentAccountSerializer,
        "DELETE": UpdateDeleteRentAccountSerializer,
    }


class AddGamesRentAccountByIdView(generics.UpdateAPIView):
    queryset = RentAccount.objects.all()
    serializer_class = AddGamesRentAccountByIdSerializer

class RemoveGamesRentAccountByIdView(generics.UpdateAPIView):
    queryset = RentAccount.objects.all()
    serializer_class = RemoveGamesRentAccountByIdSerializer

