from rest_framework import serializers

from ..go_terms.serializers import OntologyTermSerializer


class RfamClanSerializer(serializers.Serializer):
    """Serializer class for Rfam clans"""

    rfam_clan_id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    family_count = serializers.IntegerField()


class RfamModelSerializer(serializers.Serializer):
    """Serializer class for Rfam families"""

    rfam_model_id = serializers.CharField()
    short_name = serializers.CharField()
    long_name = serializers.CharField()
    description = serializers.CharField()
    rfam_clan = RfamClanSerializer(source="rfam_clan_id")
    seed_count = serializers.IntegerField()
    full_count = serializers.IntegerField()
    length = serializers.IntegerField()
    is_suppressed = serializers.BooleanField()
    domain = serializers.CharField()
    rna_type = serializers.CharField()
    rfam_rna_type = serializers.CharField()
    thumbnail_url = serializers.CharField()
    url = serializers.CharField()
    go_terms = OntologyTermSerializer(many=True)


class RfamHitsSerializer(serializers.Serializer):
    """Serializer class for Rfam Hits"""

    sequence_start = serializers.IntegerField()
    sequence_stop = serializers.IntegerField()
    sequence_completeness = serializers.FloatField()
    rfam_model = RfamModelSerializer()
