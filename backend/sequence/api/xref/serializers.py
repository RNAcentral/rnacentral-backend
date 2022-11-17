from rest_framework import serializers
from ..accession.serializers import AccessionSerializer


class XrefSerializer(serializers.Serializer):
    database = serializers.ReadOnlyField(source="db")
    is_active = serializers.ReadOnlyField(source="deleted")
    first_seen = serializers.ReadOnlyField(source="created")
    last_seen = serializers.ReadOnlyField(source="last")
    taxid = serializers.ReadOnlyField()
    accession = AccessionSerializer()
