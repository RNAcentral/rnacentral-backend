from rest_framework import serializers

from ...models import Accession


class AccessionSerializer(serializers.ModelSerializer):
    """Serializer class for individual cross-references"""
    class Meta:
        model = Accession
        fields = "__all__"
