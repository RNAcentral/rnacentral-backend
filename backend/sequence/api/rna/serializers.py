from rest_framework import serializers


class RnaSerializer(serializers.Serializer):
    """Serializer class for a unique RNAcentral sequence"""
    rnacentral_id = serializers.ReadOnlyField(source="upi")
    sequence = serializers.ReadOnlyField(source="get_sequence")
    length = serializers.ReadOnlyField()
    md5 = serializers.ReadOnlyField()
