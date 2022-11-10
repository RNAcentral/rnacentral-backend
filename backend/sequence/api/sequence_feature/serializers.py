from rest_framework import serializers


class SequenceFeatureSerializer(serializers.Serializer):
    feature_name = serializers.CharField(max_length=50, read_only=True)
    metadata = serializers.JSONField(read_only=True)
    start = serializers.IntegerField(read_only=True)
    stop = serializers.IntegerField(read_only=True)
    taxid = serializers.IntegerField(read_only=True)
    accession = serializers.StringRelatedField(read_only=True)
    upi = serializers.StringRelatedField(read_only=True)
