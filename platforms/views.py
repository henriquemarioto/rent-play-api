from rent_accounts.mixins import SerializerByMethodMixin
from rest_framework import generics

from platforms.models import Platform
from platforms.serializers import CreateListPlatformSerializer


class ListCreatePlatformView(SerializerByMethodMixin, generics.ListCreateAPIView):
    """authentication_classes = [TokenAuthentication]
    permission_classes = [ProductsPermissions]"""

    queryset = Platform.objects.all()
    serializer_map = {
        "GET": CreateListPlatformSerializer,
        "POST": CreateListPlatformSerializer,
    }
