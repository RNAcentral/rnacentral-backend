from rest_framework import serializers


class SequenceFeatureSerializer(serializers.Serializer):
    feature_name = serializers.CharField()
    metadata = serializers.JSONField(read_only=True)
    start = serializers.IntegerField()
    stop = serializers.IntegerField()
    taxid = serializers.IntegerField()
    accession = serializers.StringRelatedField(many=True)
    upi = serializers.StringRelatedField()
