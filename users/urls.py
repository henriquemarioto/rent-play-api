from django.urls import path
from .views import (
    ListUsersFilterView,
    UpdateIsActiveUserView,
    UpdateUserView,
    UserLoginView,
    UserView,
)

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<pk>/", UpdateUserView.as_view()),
    path("users/<pk>/management/", UpdateIsActiveUserView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("users/newest/<int:num>/", ListUsersFilterView.as_view()),
]
