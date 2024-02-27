from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from ..accession.serializers import AccessionSerializer
from ...models.related_sequences import RelatedSequence


def get_related_sequence(accession_id, relationship_type):
    sequence = RelatedSequence.objects.filter(
        source_accession=accession_id, relationship_type=relationship_type
    ).first()
    return sequence.target_urs_taxid_id if sequence else None


class XrefSerializer(serializers.Serializer):
    database = serializers.CharField(source="db.display_name")
    is_active = serializers.SerializerMethodField(method_name="get_deleted")
    first_seen = serializers.DateTimeField(
        source="created.release_date", format="%Y-%m-%d"
    )
    last_seen = serializers.DateTimeField(
        source="last.release_date", format="%Y-%m-%d"
    )
    taxid = serializers.IntegerField()
    accession = AccessionSerializer()
    mirbase_mature_products = serializers.SerializerMethodField(
        method_name="get_mirbase_mature_products"
    )
    mirbase_precursor = serializers.SerializerMethodField(
        method_name="get_mirbase_precursor"
    )
    refseq_mirna_mature_products = serializers.SerializerMethodField(
        method_name="get_refseq_mirna_mature_products"
    )
    refseq_mirna_precursor = serializers.SerializerMethodField(
        method_name="get_refseq_mirna_precursor"
    )
    refseq_splice_variants = serializers.SerializerMethodField(
        method_name="get_refseq_splice_variants"
    )
    ensembl_splice_variants = serializers.SerializerMethodField(
        method_name="get_ensembl_splice_variants"
    )

    @extend_schema_field(OpenApiTypes.STR)
    def get_deleted(self, obj):
        return True if obj.deleted == "N" else False

    def get_mirbase_mature_products(self, obj):
        if obj.db_id != 4:  # 4 = MIRBASE
            return None

        return get_related_sequence(obj.accession_id, "mature_product")

    def get_mirbase_precursor(self, obj):
        if obj.db_id != 4:  # 4 = MIRBASE
            return None

        return get_related_sequence(obj.accession_id, "precursor")

    def get_refseq_mirna_mature_products(self, obj):
        if obj.db_id != 9:  # 9 = REFSEQ
            return None

        return get_related_sequence(obj.accession_id, "mature_product")

    def get_refseq_mirna_precursor(self, obj):
        if obj.db_id != 9:  # 9 = REFSEQ
            return None

        return get_related_sequence(obj.accession_id, "precursor")

    def get_refseq_splice_variants(self, obj):
        if obj.db_id != 9:  # 9 = REFSEQ
            return None

        return get_related_sequence(obj.accession_id, "isoform")

    def get_ensembl_splice_variants(self, obj):
        if obj.db_id != 25:  # 25 = ENSEMBL
            return None

        return get_related_sequence(obj.accession_id, "isoform")
