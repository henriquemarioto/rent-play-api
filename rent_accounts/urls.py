from django.urls import path

from .views import (
    AddGamesRentAccountByIdView,
    ListCreateRentAccountView,
    ListRentAccountByRenterView,
    ListRentAccountBySearchView,
    ListRentAccountByUserIdView,
    ListRentAccountOwnerView,
    RemoveGamesRentAccountByIdView,
    RentRentAccountByIdView,
    RetrieveUpdateDestroyRentAccountView,
    ReturnRentAccountByIdView,
)

urlpatterns = [
    path("rent_accounts/", ListCreateRentAccountView.as_view()),
    path("rent_accounts/owner/", ListRentAccountOwnerView.as_view()),
    path("rent_accounts/renter/", ListRentAccountByRenterView.as_view()),
    path("rent_accounts/search/", ListRentAccountBySearchView.as_view()),
    path("rent_accounts/user/<pk>/", ListRentAccountByUserIdView.as_view()),
    path("rent_accounts/<pk>/", RetrieveUpdateDestroyRentAccountView.as_view()),
    path("rent_accounts/<pk>/games/add/", AddGamesRentAccountByIdView.as_view()),
    path("rent_accounts/<pk>/games/remove/", RemoveGamesRentAccountByIdView.as_view()),
    path("rent_accounts/<pk>/rent/", RentRentAccountByIdView.as_view()),
    path("rent_accounts/<pk>/return/", ReturnRentAccountByIdView.as_view()),
]
