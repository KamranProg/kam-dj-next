from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_csrf_token(request):
    return Response({"message": "CSRF cookie set"})
