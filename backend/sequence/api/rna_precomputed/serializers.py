from rest_framework import serializers


class RnaSerializer(serializers.Serializer):
    """Serializer class for a unique RNAcentral sequence"""

    rnacentral_id = serializers.CharField(source="id")
    description = serializers.CharField()
    rna_type = serializers.CharField()
    databases = serializers.CharField()
    sequence = serializers.CharField(source="upi.get_sequence")
    length = serializers.IntegerField(source="upi.length")
    md5 = serializers.CharField(source="upi.md5")


class TaxonomySerializer(serializers.Serializer):
    """Serializer class for Taxonomy"""
    urs_taxid = serializers.CharField()
    short_description = serializers.CharField()
    species_name = serializers.CharField()


class RnaPrecomputedSerializer(serializers.Serializer):
    """Serializer class used in related sequences identified by Ensembl Compara."""
    id = serializers.CharField()
    rna_type = serializers.CharField()
    description = serializers.CharField()
    databases = serializers.CharField()
