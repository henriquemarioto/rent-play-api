from django.urls import path
from .views import GameViews

urlpatterns = [
    path("games/", GameViews.as_view()),
    # path("rent_history/<pk>/", GameViewsDetail.as_view()),
]
