from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers


class DatabaseListSerializer(serializers.Serializer):
    """Serializer class for a list of Expert Databases"""

    id = serializers.IntegerField()
    descr = serializers.SerializerMethodField(method_name="get_descr")
    display_name = serializers.CharField()
    url = serializers.CharField()

    @extend_schema_field(OpenApiTypes.STR)
    def get_descr(self, obj):
        return obj.descr.lower()


class DatabaseSerializer(serializers.Serializer):
    """Serializer class for an Expert Database"""

    id = serializers.IntegerField()
    descr = serializers.CharField()
    current_release = serializers.IntegerField()
    full_descr = serializers.CharField()
    alive = serializers.CharField()
    display_name = serializers.CharField()
    avg_length = serializers.IntegerField()
    min_length = serializers.IntegerField()
    max_length = serializers.IntegerField()
    num_sequences = serializers.IntegerField()
    num_organisms = serializers.IntegerField()
    description = serializers.CharField()
    url = serializers.CharField()
    example = serializers.JSONField()
    reference = serializers.JSONField()
