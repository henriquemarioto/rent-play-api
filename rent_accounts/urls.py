from django.urls import path

from .views import ListCreateRentAccountView, RetrieveUpdateDestroyRentAccountView

urlpatterns = [
    path("rent_accounts/", ListCreateRentAccountView.as_view()),
    path("rent_accounts/<pk>/", RetrieveUpdateDestroyRentAccountView.as_view()),
    # path("rent_accounts/login/", RentAccountLoginView.as_view()),
    # path("rent_accounts/services/", RentService.as_view()),
]
