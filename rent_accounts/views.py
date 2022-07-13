from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from users.mixins import SerializerByMethodMixin

from .models import RentAccount
from .serializers import RentAccountCreateSerializer


class ListCreateRent_AccountView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = RentAccount.objects.all()
    serializer_map = {"POST": RentAccountCreateSerializer}

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
