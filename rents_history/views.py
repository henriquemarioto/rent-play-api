from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .models import RentHistory
from rent_accounts.models import RentAccount
from .serializers import RentHistorySerializer

from rent_play.permissions import OwnerAndAdminPermissions


# Create your views here.


class ListRentHistoryView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OwnerAndAdminPermissions]

    queryset = RentHistory.objects.all()
    serializer_class = RentHistorySerializer


class RetrieveRentHistoryDetailView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OwnerAndAdminPermissions]

    queryset = RentHistory.objects.all()
    serializer_class = RentHistorySerializer

class ListRentHistoryRentedByOtherUsersView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OwnerAndAdminPermissions]

    serializer_class = RentHistorySerializer

    def get_queryset(self):
        user = self.request.user
        return RentHistory.objects.filter(rent_account__owner__id=user.id)

class ListRentHistoryUserRentedView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OwnerAndAdminPermissions]

    serializer_class = RentHistorySerializer

    def get_queryset(self):
        user = self.request.user
        
        return RentHistory.objects.filter(renter=user.id)
