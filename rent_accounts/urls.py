from django.urls import path

from .views import ListCreateRent_AccountView  #RentService, RentViews,  RentViewsDetail,RentAccountLoginView

urlpatterns = [
    path("rent_accounts/", ListCreateRent_AccountView.as_view()),
    # path("rent_accounts/<pk>/", RentViewsDetail.as_view()),
    #path("rent_accounts/login/", RentAccountLoginView.as_view()),
    #path("rent_accounts/services/", RentService.as_view()),
]
