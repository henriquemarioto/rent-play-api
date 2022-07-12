from django.urls import path
from .views import (
    RentViews,
    # RentViewsDetail,
    RentAccountLoginView,
    RentService,
)

urlpatterns = [
    path("rent_accounts/", RentViews.as_view()),
    # path("rent_accounts/<pk>/", RentViewsDetail.as_view()),
    path("rent_accounts/login/", RentAccountLoginView.as_view()),
    path("rent_accounts/services/", RentService.as_view()),
]
