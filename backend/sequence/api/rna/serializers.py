from rest_framework import serializers


class RnaSerializer(serializers.Serializer):
    """Serializer class for a unique RNAcentral sequence"""
    rnacentral_id = serializers.CharField(source="upi", max_length=13, read_only=True)
    sequence = serializers.CharField(source="get_sequence", read_only=True)
    length = serializers.IntegerField(read_only=True)
    md5 = serializers.CharField(max_length=32, read_only=True)
