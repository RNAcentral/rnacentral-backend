import re

from rest_framework import serializers
from ..ensembl_assembly.serializers import EnsemblAssemblySerializer


class SequenceRegionSerializer(serializers.Serializer):
    """Serializer class for Sequence Region"""
    chromosome = serializers.ReadOnlyField()
    strand = serializers.ReadOnlyField()
    start = serializers.ReadOnlyField(source="region_start")
    end = serializers.ReadOnlyField(source="region_stop")
    identity = serializers.ReadOnlyField()
    databases = serializers.SerializerMethodField(method_name="get_providing_databases")
    ucsc_chromosome = serializers.SerializerMethodField(method_name="get_chromosome")
    ensembl_assembly = EnsemblAssemblySerializer(source="assembly")

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

    def get_chromosome(self, obj):
        exceptions = ["X", "Y"]
        if re.match(r"\d+", obj.chromosome) or obj.chromosome in exceptions:
            ucsc_chromosome = "chr" + obj.chromosome
        else:
            ucsc_chromosome = obj.chromosome

        return ucsc_chromosome
