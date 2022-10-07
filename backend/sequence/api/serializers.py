from rest_framework import serializers

from ..models import SequenceFeature


class SequenceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SequenceFeature
        fields = "__all__"
