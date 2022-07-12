from rest_framework import generics
from rest_framework.views import Response, status
from django.contrib.auth import authenticate
from .models import RentAccount
from .serializers import RentAccauntSerializer, RentAccountLogin
from users.mixins import SerializerByMethodMixin
from rest_framework.authtoken.models import Token


class RentAccountViews(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = RentAccount.all()
    serializer_map = {"POST": RentAccauntSerializer, "GET": RentAccauntSerializer}


class RentAccountLoginView(generics.CreateAPIView):
    def post(self, request):
        serializer = RentAccountLogin(data=request.data)
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