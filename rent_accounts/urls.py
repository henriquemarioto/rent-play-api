from django.urls import path

from .views import (
    ListCreateRentAccountView,
    RetrieveUpdateDestroyRentAccountView,
    AddGamesRentAccountByIdView,
    RemoveGamesRentAccountByIdView,
    ListRentAccountOwnerView,
    ListRentAccountByUserIdView,
    ListRentAccountByRenterView,
    RentRentAccountByIdView,
    ReturnRentAccountByIdView,
)

urlpatterns = [
    path("rent_accounts/", ListCreateRentAccountView.as_view()),
    path("rent_accounts/owner/", ListRentAccountOwnerView.as_view()),
    path("rent_accounts/search/", ListRentAccountByUserIdView.as_view()),
    path("rent_accounts/user/<pk>/", ListRentAccountByUserIdView.as_view()),
    path("rent_accounts/<pk>/", RetrieveUpdateDestroyRentAccountView.as_view()),
    path("rent_accounts/<pk>/games/add/", AddGamesRentAccountByIdView.as_view()),
    path("rent_accounts/<pk>/games/remove/", RemoveGamesRentAccountByIdView.as_view()),
    path("rent_accounts/<pk>/rent/", RentRentAccountByIdView.as_view()),
    path("rent_accounts/<pk>/return/", ReturnRentAccountByIdView.as_view()),
]
