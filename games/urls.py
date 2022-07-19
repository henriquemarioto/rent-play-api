from django.urls import path
from .views import GameViews, RetrieveUpdateDestroyGameView


urlpatterns = [
    path("games/", GameViews.as_view()),
    path("games/<pk>/", RetrieveUpdateDestroyGameView.as_view()),   
]
