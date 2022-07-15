from rent_accounts.mixins import SerializerByMethodMixin
from rest_framework import generics

from platforms.models import Platform
from platforms.serializers import PlatformSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ListCreatePlatformView(SerializerByMethodMixin, generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Platform.objects.all()
    serializer_map = {
        "GET": PlatformSerializer,
        "POST": PlatformSerializer,
    }
