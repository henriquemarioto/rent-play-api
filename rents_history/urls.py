from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
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
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
