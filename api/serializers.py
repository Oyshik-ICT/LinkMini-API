from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from rest_framework import serializers

from .models import UrlMapping


class UrlMappingSerializer(serializers.ModelSerializer):
    """
    Serializer for the UrlMapping model, including validation for the `long_url` field.
    Fields are read-only except for `long_url`.
    """

    class Meta:
        model = UrlMapping
        fields = (
            "id",
            "short_url",
            "long_url",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "short_url": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def validate_long_url(self, value):
        validate = URLValidator()
        try:
            validate(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid URL format")
        return value
