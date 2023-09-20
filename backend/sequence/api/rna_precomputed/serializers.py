from rest_framework import serializers

from ...models.rna_precomputed import RnaPrecomputed


class RnaSerializer(serializers.Serializer):
    """Serializer class for a unique RNAcentral sequence"""

    rnacentral_id = serializers.ReadOnlyField(source="id")
    description = serializers.ReadOnlyField()
    rna_type = serializers.ReadOnlyField()
    databases = serializers.ReadOnlyField()
    sequence = serializers.ReadOnlyField(source="upi.get_sequence")
    length = serializers.ReadOnlyField(source="upi.length")
    md5 = serializers.ReadOnlyField(source="upi.md5")


class TaxonomySerializer(serializers.Serializer):
    urs_taxid = serializers.ReadOnlyField()
    short_description = serializers.ReadOnlyField()
    species_name = serializers.ReadOnlyField()


class RnaPrecomputedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RnaPrecomputed
        fields = ("id", "rna_type", "description", "databases")
