from rest_framework import serializers


class SequenceFeatureSerializer(serializers.Serializer):
    feature_name = serializers.ReadOnlyField()
    metadata = serializers.JSONField(read_only=True)
    start = serializers.ReadOnlyField()
    stop = serializers.ReadOnlyField()
    taxid = serializers.ReadOnlyField()
    accession = serializers.StringRelatedField(many=True)
    upi = serializers.StringRelatedField()
