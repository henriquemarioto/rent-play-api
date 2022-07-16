from django.shortcuts import get_object_or_404
from rent_play.permissions import OwnerAndAdminPermissions, RenterAndOwnerPermissions
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, status
from users.mixins import SerializerByMethodMixin
from users.models import User

from .models import RentAccount
from .serializers import (
    AddGamesRentAccountByIdSerializer,
    CreateRentAccountSerializer,
    ListAndRetriveRentAccountSerializer,
    RemoveGamesRentAccountByIdSerializer,
    UpdateDeleteRentAccountSerializer,
    UpdateRentRentAccountByIdSerializer,
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


class UpdateRentRentAccountByIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            rent_account = get_object_or_404(RentAccount, pk=pk)
            if rent_account.renter:
                return Response({"message": "Account is already being rented!"}, status.HTTP_403_FORBIDDEN)

            account_owner = get_object_or_404(User, rent_account.owner)
            renter = request.user
            

            serializer = UpdateRentRentAccountByIdSerializer(
                rent_account, request.data, partial=True
            )

            serializer.is_valid(raise_exception=True)

            serializer.save(renter=request.user)

            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({"message": "Account not found"}, status.HTTP_404_NOT_FOUND)
