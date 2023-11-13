import re

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from ..ensembl_assembly.serializers import EnsemblAssemblySerializer


class SequenceRegionSerializer(serializers.Serializer):
    """Serializer class for Sequence Region"""

    chromosome = serializers.CharField()
    strand = serializers.IntegerField()
    start = serializers.IntegerField(source="region_start")
    end = serializers.IntegerField(source="region_stop")
    identity = serializers.IntegerField()
    databases = serializers.SerializerMethodField(method_name="get_providing_databases")
    ucsc_chromosome = serializers.SerializerMethodField(method_name="get_chromosome")
    ensembl_assembly = EnsemblAssemblySerializer(source="assembly")

    @extend_schema_field(OpenApiTypes.STR)
    def get_providing_databases(self, obj):
        if len(obj.providing_databases) > 1:
            databases = " and ".join(
                [
                    ", ".join(obj.providing_databases[:-1]),
                    obj.providing_databases[-1],
                ]
            )
        elif len(obj.providing_databases) == 1:
            databases = obj.providing_databases[0]
        else:
            databases = None

        return databases

    @extend_schema_field(OpenApiTypes.STR)
    def get_chromosome(self, obj):
        exceptions = ["X", "Y"]
        if re.match(r"\d+", obj.chromosome) or obj.chromosome in exceptions:
            ucsc_chromosome = "chr" + obj.chromosome
        else:
            ucsc_chromosome = obj.chromosome

        return ucsc_chromosome
