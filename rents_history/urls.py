from django.urls import path
from .views import (
    ListRentHistoryView,
    RetrieveRentHistoryDetailView,
    CreateRentHistoryView,
)

urlpatterns = [
    path("rent_history/", ListRentHistoryView.as_view()),
    path("rent_history/<pk>/", RetrieveRentHistoryDetailView.as_view()),
    path("rent_history/create/<rent_account_pk>/", CreateRentHistoryView.as_view()),
]
