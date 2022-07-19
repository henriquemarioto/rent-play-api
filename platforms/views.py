from platforms.exceptions import PlatformAlreadyExistsInDataBase
from rent_accounts.mixins import SerializerByMethodMixin
from rest_framework import generics

from platforms.models import Platform
from platforms.serializers import PlatformSerializer

from rest_framework.authentication import TokenAuthentication

from users.permissions import SuperUserPermissions


class ListCreatePlatformView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserPermissions]

    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

    def perform_create(self, serializer):
        platform_api_id_data = Platform.objects.filter(
            platform_api_id=self.request.data["platform_api_id"]
        )

        platform_name_data = Platform.objects.filter(
            name=self.request.data["name"]
        )

        if platform_api_id_data or platform_name_data:
            raise PlatformAlreadyExistsInDataBase
        
        serializer.save()

class RetrieveUpdateDestroyPlatformView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserPermissions]

    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer