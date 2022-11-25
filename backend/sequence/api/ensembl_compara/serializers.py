from rest_framework import serializers

from ..rna_precomputed.serializers import RnaPrecomputedSerializer


class EnsemblComparaSerializer(serializers.Serializer):
    """Serializer class for Ensembl Compara"""
    ensembl_transcript_id = serializers.ReadOnlyField()
    rnacentral_id = RnaPrecomputedSerializer(source="urs_taxid")
