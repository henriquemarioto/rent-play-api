from django.urls import path
from .views import (
    HistoryViews,
    HistoryViewsDetail
)

urlpatterns = [
    path("rent_history/", HistoryViews.as_view()),
    path("rent_history/<pk>/", HistoryViewsDetail.as_view()),   
    
]