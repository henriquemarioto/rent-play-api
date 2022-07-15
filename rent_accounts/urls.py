from django.urls import path

from .views import ListCreateRentAccountView, RetrieveUpdateDestroyRentAccountView, AddGamesRentAccountByIdView, RemoveGamesRentAccountByIdView, UpdateRentRentAccountByIdView

urlpatterns = [
    path("rent_accounts/", ListCreateRentAccountView.as_view()),
    path("rent_accounts/<pk>/", RetrieveUpdateDestroyRentAccountView.as_view()),
    path("rent_accounts/<pk>/games/add/", AddGamesRentAccountByIdView.as_view()),
    path("rent_accounts/<pk>/games/remove/", RemoveGamesRentAccountByIdView.as_view()),
    path("rent_accounts/<pk>/rent/",  UpdateRentRentAccountByIdView.as_view())
]
