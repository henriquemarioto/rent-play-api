from rest_framework import generics
from rest_framework.views import Response, status
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from users.mixins import SerializerByMethodMixin
from users.permissions import (
    CreateUserPermissions,
    SuperUserPermissions,
    UserPermissions,
)
from .models import User
from rest_framework.authtoken.models import Token
from .serializers import IsActiveUserSerializer, UserLoginSerializer, UserSerializer


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
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        max_users = self.kwargs["num"]
        return self.queryset.order_by("-date_joined")[0:max_users]


class UpdateUserView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UserPermissions, SuperUserPermissions]

    def show(self, request):
        print("AQUIIIIIIIIIIIIIIIIIII", self.request.user)

    queryset = User.objects.all()
    serializer_map = {"PATCH": UserSerializer, "GET": UserSerializer}


class UpdateIsActiveUserView(SerializerByMethodMixin, generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserPermissions]

    queryset = User.objects.all()
    serializer_map = {"PATCH": IsActiveUserSerializer}
