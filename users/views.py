from rest_framework import generics
from rest_framework.views import Response, status
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication

from users.mixins import SerializerByMethodMixin
from users.permissions import CreateUserPermissions, SuperUserPermissions, UserPermissions
from .models import User
from rest_framework.authtoken.models import Token
from .serializers import UserLoginSerializer, UserSerializer


class UserView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CreateUserPermissions]

    queryset = User.objects.all().order_by("id")
    serializer_map = {"POST": UserSerializer, "GET": UserSerializer}


class UserLoginView(generics.CreateAPIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

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


class UpdateUserView(SerializerByMethodMixin, generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermissions]

    queryset = User.objects.all()
    serializer_map = {"PATCH": UserSerializer}
