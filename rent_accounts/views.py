import datetime
from decimal import Decimal

from django.shortcuts import get_object_or_404
from platforms.models import Platform
from rent_play.permissions import OwnerAndAdminPermissions, RenterAndOwnerPermissions
from rents_history.models import RentHistory
from rents_history.serializers import RentHistorySerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, status
from users.mixins import SerializerByMethodMixin
from users.models import User
from .exceptions import EmailAlreadyExistInThisPlatform

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
        login = self.request.data["login"]
        platform = get_object_or_404(Platform, pk=self.request.data["platform"])
        rent_account = RentAccount.objects.filter(login=login, platform=platform)
        
        if rent_account:
            raise EmailAlreadyExistInThisPlatform
        serializer.save(owner=self.request.user, platform=platform)


class ListRentAccountUserbyIdView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ListAndRetriveRentAccountSerializer

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs["pk"])
        return RentAccount.objects.filter(owner=user.id)


class ListRentAccountOwnerView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ListAndRetriveRentAccountSerializer
    
    def get_queryset(self):
        user = get_object_or_404(User, pk=self.request.user.id)
        return RentAccount.objects.filter(owner=user)


class ListRentAccountUserbyRenterView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ListAndRetriveRentAccountSerializer
    
    def get_queryset(self):
        user = get_object_or_404(User, pk=self.request.user.id)
        return RentAccount.objects.filter(renter=user)



class RetrieveUpdateDestroyRentAccountView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OwnerAndAdminPermissions]

    queryset = RentAccount.objects.all()
    serializer_map = {
        "GET": ListAndRetriveRentAccountSerializer,
        "PATCH": UpdateDeleteRentAccountSerializer,
        "DELETE": UpdateDeleteRentAccountSerializer,
    }


class AddGamesRentAccountByIdView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OwnerAndAdminPermissions]

    queryset = RentAccount.objects.all()
    serializer_class = AddGamesRentAccountByIdSerializer


class RemoveGamesRentAccountByIdView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OwnerAndAdminPermissions]

    queryset = RentAccount.objects.all()
    serializer_class = RemoveGamesRentAccountByIdSerializer


class RentRentAccountByIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        try:
            rent_account = get_object_or_404(RentAccount, pk=pk)
        except:
            return Response({"message": "Account not found"}, status.HTTP_404_NOT_FOUND)

        renter = self.request.user
        admin = get_object_or_404(User, email="admin@rentandplay.com.br")
        account_owner = get_object_or_404(User, email=rent_account.owner.email)

        if rent_account.renter:
            return Response(
                {"message": "Account is already being rented!"},
                status.HTTP_403_FORBIDDEN,
            )

        days = [3, 7, 14, 30]
        if not request.data["rented_days"] in days:
            return Response(
                {"message": f"Invalid rented_days, must be {days}"},
                status.HTTP_400_BAD_REQUEST,
            )

        total_price = Decimal(rent_account.price_per_day * request.data["rented_days"])

        user_money = Decimal(renter.wallet)
        if user_money < total_price:
            return Response(
                {"message": "Wallet funds is not enough to rent this account!"},
                status.HTTP_403_FORBIDDEN,
            )

        rent_history_data = {
            "end_date": datetime.datetime.now()
            + datetime.timedelta(days=request.data["rented_days"]),
            "total_price": total_price,
        }

        renter.wallet -= total_price

        admin_value = Decimal((15 / 100)) * total_price
        owner_value = Decimal((85 / 100)) * total_price

        admin.wallet += admin_value
        account_owner.wallet += owner_value

        admin.save()
        renter.save()
        account_owner.save()

        rent_account.renter = renter
        rent_account.save()

        rent_history_serializer = RentHistorySerializer(data=rent_history_data)
        rent_history_serializer.is_valid(raise_exception=True)
        rent_history_serializer.save(renter=renter, rent_account=rent_account)

        return Response(rent_history_serializer.data, status.HTTP_200_OK)


class ReturnRentAccountByIdView(APIView):

    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        rent_account = get_object_or_404(RentAccount, pk=pk)

        try:
            rent_history = get_object_or_404(
                RentHistory, rent_account=rent_account, return_date=None
            )
        except:
            return Response({"message": "This account is already being returned!"}, status.HTTP_404_NOT_FOUND)

        rent_history.return_date = datetime.datetime.now()

        rent_account.renter = None

        rent_account.save()
        rent_history.save()

        return Response({"message": "OK"})


