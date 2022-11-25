from rest_framework import serializers
from ..accession.serializers import AccessionSerializer


class XrefSerializer(serializers.Serializer):
    database = serializers.ReadOnlyField(source="db.display_name")
    is_active = serializers.SerializerMethodField(method_name="get_deleted")
    first_seen = serializers.ReadOnlyField(source="created.release_date")
    last_seen = serializers.ReadOnlyField(source="last.release_date")
    taxid = serializers.ReadOnlyField()
    accession = AccessionSerializer()

    def get_deleted(self, obj):
        return True if obj.deleted == "N" else False
