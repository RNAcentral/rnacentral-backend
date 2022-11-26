from rest_framework import serializers


class TargetLncRNAsSerializer(serializers.Serializer):
    """Serializer class for target lncRNAs"""
    source_accession = serializers.ReadOnlyField()
    target_accession = serializers.ReadOnlyField()
    methods = serializers.ReadOnlyField()
    target_urs_taxid = serializers.PrimaryKeyRelatedField(read_only=True)
    # protein_info = ProteinInfoSerializer(read_only=True, many=True)


class TargetMiRNAsSerializer(serializers.Serializer):
    """Serializer class for target miRNAs"""
    short_description = serializers.ReadOnlyField(source="source_urs_taxid.short_description")
    source_urs_taxid = serializers.PrimaryKeyRelatedField(read_only=True)
