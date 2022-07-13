from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .models import RentHistory
from rent_accounts.models import RentAccount
from .serializers import RentHistorySerializer

from rents_history.mixins import SerializerByMethodMixin


# Create your views here.


class ListRentHistoryView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = RentHistory.objects.all()
    serializer_class = RentHistorySerializer


class CreateRentHistoryView(SerializerByMethodMixin, generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = RentHistory.objects.all()
    serializer_map = {"POST": RentHistorySerializer}

    def perform_create(self, serializer):
        rent_account_id = self.kwargs["rent_account_pk"]

        rent_account = get_object_or_404(RentAccount, pk=rent_account_id)

        serializer.save(user=[self.request.user], rent_accounts=[rent_account])


class RetrieveRentHistoryDetailView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = RentHistory.objects.all()
    serializer_class = RentHistorySerializer
