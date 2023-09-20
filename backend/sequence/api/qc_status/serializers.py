from rest_framework import serializers


class QcStatusSerializer(serializers.Serializer):
    """Serializer class for QC Status"""

    id = serializers.PrimaryKeyRelatedField(read_only=True)
    has_issue = serializers.ReadOnlyField()
    incomplete_sequence = serializers.ReadOnlyField()
    possible_contamination = serializers.ReadOnlyField()
    missing_rfam_match = serializers.ReadOnlyField()
    from_repetitive_region = serializers.ReadOnlyField()
    possible_orf = serializers.ReadOnlyField()
    messages = serializers.JSONField(read_only=True)
