from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers


class EnsemblAssemblySerializer(serializers.Serializer):
    """Serializer class for Ensembl Assembly"""

    assembly_id = serializers.CharField()
    species = serializers.CharField(source="ensembl_url")
    ucsc_db_id = serializers.CharField(source="assembly_ucsc")
    ensembl_division_name = serializers.CharField(source="division")
    ensembl_division_url = serializers.SerializerMethodField(
        method_name="get_subdomain"
    )
    ensembl_species_url = serializers.CharField(source="ensembl_url")

    @extend_schema_field(OpenApiTypes.STR)
    def get_subdomain(self, obj):
        return f"http://{obj.subdomain}"
