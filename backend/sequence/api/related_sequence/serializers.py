from rest_framework import serializers


class TargetLncRNAsSerializer(serializers.Serializer):
    """Serializer class for target lncRNAs"""

    target_accession = serializers.CharField()
    source_accession = serializers.CharField()
    # description = serializers.ReadOnlyField(source="target_accession.description")
    # label = serializers.ReadOnlyField(source="target_accession.label")
    # synonyms = serializers.ReadOnlyField(source="target_accession.synonyms")
    methods = serializers.ReadOnlyField()
    target_urs_taxid = serializers.CharField()


class TargetMiRNAsSerializer(serializers.Serializer):
    """Serializer class for target miRNAs"""

    short_description = serializers.CharField(
        source="source_urs_taxid.short_description"
    )
    source_urs_taxid = serializers.CharField()


class TargetProteinsSerializer(serializers.Serializer):
    """Serializer class for target proteins"""

    target_accession = serializers.CharField()
    source_accession = serializers.CharField()
    # description = serializers.ReadOnlyField(source="target_accession.description")
    # label = serializers.ReadOnlyField(source="target_accession.label")
    # synonyms = serializers.ReadOnlyField(source="target_accession.synonyms")
    methods = serializers.ReadOnlyField()
