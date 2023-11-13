from rest_framework import serializers


class GoTermsSerializer(serializers.Serializer):
    """Serializer class for GO terms"""

    go_term_id = serializers.CharField(source="ontology_term")
    go_term_name = serializers.CharField(source="ontology_term.name")
    qualifier = serializers.CharField()
    evidence_code_id = serializers.CharField(source="evidence_code")
    evidence_code_name = serializers.CharField(source="evidence_code.name")
    assigned_by = serializers.CharField()
    quickgo_url = serializers.CharField(source="ontology_term.quickgo_url")


class OntologyTermSerializer(serializers.Serializer):
    ontology_term_id = serializers.CharField()
    ontology = serializers.CharField()
    name = serializers.CharField()
    definition = serializers.CharField()
    url = serializers.CharField()
    quickgo_url = serializers.CharField()
