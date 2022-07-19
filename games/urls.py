from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.urls import path
from .views import GameViews, RetrieveUpdateDestroyGameView

urlpatterns = [
    path("games/", GameViews.as_view()),
    path("games/<pk>/", RetrieveUpdateDestroyGameView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
