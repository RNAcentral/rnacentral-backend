from rest_framework import serializers

from ...models.rna_precomputed import RnaPrecomputed


class RnaPrecomputedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RnaPrecomputed
        fields = ("id", "rna_type", "description", "databases")
