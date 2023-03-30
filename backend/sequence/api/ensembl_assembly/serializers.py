from rest_framework import serializers


class EnsemblAssemblySerializer(serializers.Serializer):
    """Serializer class for Ensembl Assembly"""
    assembly_id = serializers.ReadOnlyField()
    species = serializers.ReadOnlyField(source="ensembl_url")
    ucsc_db_id = serializers.ReadOnlyField(source="assembly_ucsc")
    ensembl_division_name = serializers.ReadOnlyField(source="division")
    ensembl_division_url = serializers.SerializerMethodField(method_name="get_subdomain")
    ensembl_species_url = serializers.ReadOnlyField(source="ensembl_url")

    def get_subdomain(self, obj):
        return f"http://{obj.subdomain}"
