from rest_framework import serializers

from ..go_terms.serializers import OntologyTermSerializer


class RfamClanSerializer(serializers.Serializer):
    """Serializer class for Rfam clans"""
    rfam_clan_id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    family_count = serializers.ReadOnlyField()


class RfamModelSerializer(serializers.Serializer):
    """Serializer class for Rfam families"""
    rfam_model_id = serializers.ReadOnlyField()
    short_name = serializers.ReadOnlyField()
    long_name = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    rfam_clan = RfamClanSerializer(source="rfam_clan_id")
    seed_count = serializers.ReadOnlyField()
    full_count = serializers.ReadOnlyField()
    length = serializers.ReadOnlyField()
    is_suppressed = serializers.ReadOnlyField()
    domain = serializers.ReadOnlyField()
    rna_type = serializers.ReadOnlyField()
    rfam_rna_type = serializers.ReadOnlyField()
    thumbnail_url = serializers.ReadOnlyField()
    url = serializers.ReadOnlyField()
    go_terms = OntologyTermSerializer(many=True)


class RfamHitsSerializer(serializers.Serializer):
    """Serializer class for Rfam Hits"""
    sequence_start = serializers.ReadOnlyField()
    sequence_stop = serializers.ReadOnlyField()
    sequence_completeness = serializers.ReadOnlyField()
    rfam_model = RfamModelSerializer()
