from rent_accounts.mixins import SerializerByMethodMixin
from rest_framework import generics

from platforms.models import Platform
from platforms.serializers import PlatformSerializer

from rest_framework.authentication import TokenAuthentication

from users.permissions import SuperUserPermissions


class ListCreatePlatformView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserPermissions]

    queryset = Platform.objects.all()
    serializer_map = {
        "GET": PlatformSerializer,
        "POST": PlatformSerializer,
    }
