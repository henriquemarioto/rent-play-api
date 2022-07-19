from django.urls import path

from .views import ListCreatePlatformView

urlpatterns = [
    path("platforms/", ListCreatePlatformView.as_view()),
]
