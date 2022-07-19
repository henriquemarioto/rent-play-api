from django.urls import path

from .views import ListCreatePlatformView, RetrieveUpdateDestroyPlatformView

urlpatterns = [
    path("platforms/", ListCreatePlatformView.as_view()),
    path("platforms/<pk>/", RetrieveUpdateDestroyPlatformView.as_view()),
]
