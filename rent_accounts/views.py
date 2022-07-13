from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
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
        serializer.save(owner=self.request.user)


class RetrieveUpdateDestroyRentAccountView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    queryset = RentAccount.objects.all()
    serializer_map = {
        "GET": ListAndRetriveRentAccountSerializer,
        "PATCH": UpdateDeleteRentAccountSerializer,
        "DELETE": UpdateDeleteRentAccountSerializer,
    }

