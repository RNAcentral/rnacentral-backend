from rest_framework import serializers


class TargetLncRNAsSerializer(serializers.Serializer):
    """Serializer class for target lncRNAs"""

    target_accession = serializers.ReadOnlyField()
    source_accession = serializers.ReadOnlyField()
    # description = serializers.ReadOnlyField(source="target_accession.description")
    # label = serializers.ReadOnlyField(source="target_accession.label")
    # synonyms = serializers.ReadOnlyField(source="target_accession.synonyms")
    methods = serializers.ReadOnlyField()
    target_urs_taxid = serializers.PrimaryKeyRelatedField(read_only=True)


class TargetMiRNAsSerializer(serializers.Serializer):
    """Serializer class for target miRNAs"""

    short_description = serializers.ReadOnlyField(
        source="source_urs_taxid.short_description"
    )
    source_urs_taxid = serializers.PrimaryKeyRelatedField(read_only=True)


class TargetProteinsSerializer(serializers.Serializer):
    """Serializer class for target proteins"""

    target_accession = serializers.ReadOnlyField()
    source_accession = serializers.ReadOnlyField()
    # description = serializers.ReadOnlyField(source="target_accession.description")
    # label = serializers.ReadOnlyField(source="target_accession.label")
    # synonyms = serializers.ReadOnlyField(source="target_accession.synonyms")
    methods = serializers.ReadOnlyField()
