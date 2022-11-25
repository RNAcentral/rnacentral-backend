from rest_framework import serializers


class GoTermsSerializer(serializers.Serializer):
    """Serializer class for GO terms"""
    go_term_id = serializers.PrimaryKeyRelatedField(
        source="ontology_term",
        read_only=True
    )
    go_term_name = serializers.ReadOnlyField(
        source="ontology_term.name"
    )
    qualifier = serializers.ReadOnlyField()
    evidence_code_id = serializers.PrimaryKeyRelatedField(
        source="evidence_code",
        read_only=True
    )
    evidence_code_name = serializers.ReadOnlyField(
        source="evidence_code.name"
    )
    assigned_by = serializers.ReadOnlyField()
    quickgo_url = serializers.ReadOnlyField(
        source="ontology_term.quickgo_url"
    )


class OntologyTermSerializer(serializers.Serializer):
    ontology_term_id = serializers.ReadOnlyField()
    ontology = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    definition = serializers.ReadOnlyField()
    url = serializers.ReadOnlyField()
    quickgo_url = serializers.ReadOnlyField()
