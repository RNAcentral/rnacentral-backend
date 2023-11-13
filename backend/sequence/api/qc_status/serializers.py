from rest_framework import serializers


class QcStatusSerializer(serializers.Serializer):
    """Serializer class for QC Status"""

    id = serializers.CharField(source="id.id")
    has_issue = serializers.BooleanField()
    incomplete_sequence = serializers.BooleanField()
    possible_contamination = serializers.BooleanField()
    missing_rfam_match = serializers.BooleanField()
    from_repetitive_region = serializers.BooleanField()
    possible_orf = serializers.BooleanField()
    messages = serializers.JSONField(read_only=True)
