from collections.abc import Sequence

from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .views import get_csrf_token


class HealthCheckView(APIView):
    authentication_classes: Sequence[type[BaseAuthentication]] = []
    permission_classes: Sequence[type[BasePermission]] = []

    def get(self, request: Request) -> Response:
        return Response({"status": "ok"})


urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    # CSRF token endpoint
    path("auth/csrf/", get_csrf_token, name="get_csrf_token"),
    # Schema + Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
