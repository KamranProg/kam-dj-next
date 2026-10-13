from typing import Any

from rest_framework import serializers


class NoTokenSerializer(serializers.Serializer[Any]):
    """Stand-in for dj-rest-auth's token serializer.

    API tokens are disabled (``TOKEN_MODEL`` is ``None``), so nothing is ever
    serialized. dj-rest-auth's default serializer has no model in that case,
    which breaks OpenAPI schema generation.
    """
