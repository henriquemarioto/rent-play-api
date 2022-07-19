from django.urls import path
from .views import (
    ListRentHistoryView,
    RetrieveRentHistoryDetailView,
    ListRentHistoryRentedByOtherUsersView,
    ListRentHistoryUserRentedView
)

urlpatterns = [
    path("rent_histories/", ListRentHistoryView.as_view()),
    path("rent_histories/owner/", ListRentHistoryRentedByOtherUsersView.as_view()),
    path("rent_histories/rented/", ListRentHistoryUserRentedView.as_view()),
    path("rent_histories/<pk>/", RetrieveRentHistoryDetailView.as_view()),
]
