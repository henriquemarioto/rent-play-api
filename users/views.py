from decimal import Decimal
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from rent_accounts.models import RentAccount
from users.exceptions import KeyIsRequired, WalletWithoutFunds

from users.mixins import SerializerByMethodMixin
from users.permissions import (
    CreateUserPermissions,
    OrSuperUserPermissions,
    SuperUserPermissions,
    UserPermissions,
)

from .models import User
from .serializers import (
    GetUserWithWalletSerializer,
    IsActiveUserSerializer,
    UpdateUserSerializer,
    UpdateUserWalletSerializer,
    UpdateUserWalletWithdrawSerializer,
    UserLoginSerializer,
    UserSerializer,
)


class UserView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CreateUserPermissions]

    queryset = User.objects.all().order_by("id")
    serializer_map = {"POST": UserSerializer, "GET": UserSerializer}

class UserLoginView(generics.CreateAPIView):
    queryset = User
    serializer_class = UserLoginSerializer

    def post(self, request):

        login_serializer = UserLoginSerializer(data=request.data)

        login_serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=login_serializer.validated_data["email"],
            password=login_serializer.validated_data["password"],
        )        

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            user.user = user
            user.token = token.key
            login_serializer = UserLoginSerializer(user)
            return Response(login_serializer.data)

        return Response(
            {"detail": "invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class ListUsersFilterView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        max_users = self.kwargs["num"]
        return self.queryset.order_by("-date_joined")[0:max_users]


class UpdateUserView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermissions]

    queryset = User.objects.all()
    serializer_map = {"PATCH": UpdateUserSerializer, "GET": UserSerializer}

    def retrieve(self, request, *args, **kwargs):
        user = self.request.user
        user_url = get_object_or_404(User, pk=kwargs["pk"])
        
        if user.id == user_url.id:
            serializer = GetUserWithWalletSerializer(user_url)
        else:
            serializer = self.get_serializer(user_url)

        return Response(serializer.data)
        
class UpdateUserWalletView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OrSuperUserPermissions]

    queryset = User.objects.all()
    serializer_class = UpdateUserWalletSerializer

    def perform_update(self, serializer):
        if not self.request.data.get("wallet"):
            raise KeyIsRequired
        
        serializer.save()

class UpdateUserWalletWithdrawView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OrSuperUserPermissions]

    queryset = User.objects.all()
    serializer_class = UpdateUserWalletWithdrawSerializer

    def perform_update(self, serializer):
        user = self.request.user
        
        if user.wallet < Decimal(self.request.data.get("wallet")):
            raise WalletWithoutFunds

        if not self.request.data.get("wallet"):
            raise KeyIsRequired
        
        serializer.save()


class UpdateIsActiveUserView(SerializerByMethodMixin, generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserPermissions]

    queryset = User.objects.all()
    serializer_map = {"PATCH": IsActiveUserSerializer}
