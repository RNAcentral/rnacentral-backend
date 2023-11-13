from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from ..accession.serializers import AccessionSerializer


class XrefSerializer(serializers.Serializer):
    database = serializers.CharField(source="db.display_name")
    is_active = serializers.SerializerMethodField(method_name="get_deleted")
    first_seen = serializers.DateTimeField(
        source="created.release_date", format="%Y-%m-%d"
    )
    last_seen = serializers.DateTimeField(
        source="last.release_date", format="%Y-%m-%d"
    )
    taxid = serializers.IntegerField()
    accession = AccessionSerializer()

    @extend_schema_field(OpenApiTypes.STR)
    def get_deleted(self, obj):
        return True if obj.deleted == "N" else False
