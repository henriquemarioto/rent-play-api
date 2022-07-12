from django.urls import path
from .views import (
    GameViews,
    GameViewsDetail
)

urlpatterns = [
    path("rent_history/", GameViews.as_view()),
    path("rent_history/<pk>/", GameViewsDetail.as_view()),   
    
]