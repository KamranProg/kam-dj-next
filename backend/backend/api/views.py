from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response


@ensure_csrf_cookie
@api_view(["GET"])
@renderer_classes([JSONRenderer])
def get_csrf_token(request: Request) -> Response:
    """Endpoint to set the CSRF cookie.

    Returns:
        Response: A response indicating the CSRF cookie has been set.

    """
    return Response({"message": "CSRF cookie set"})
