import json
import requests

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

    # database-specific fields
    ensembl_url = serializers.SerializerMethodField(
        method_name="get_ensembl_url"
    )
    ensembl_splice_variants = serializers.SerializerMethodField(
        method_name="get_ensembl_splice_variants"
    )
    gencode_ensembl_url = serializers.SerializerMethodField(
        method_name="get_gencode_ensembl_url"
    )
    gencode_transcript_id = serializers.SerializerMethodField(
        method_name="get_gencode_transcript_id"
    )
    mirbase_mature_products = serializers.SerializerMethodField(
        method_name="get_mirbase_mature_products"
    )
    mirbase_precursor = serializers.SerializerMethodField(
        method_name="get_mirbase_precursor"
    )
    quickgo_hits = serializers.SerializerMethodField(
        method_name="get_quickgo_hits"
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

    @extend_schema_field(OpenApiTypes.STR)
    def get_deleted(self, obj):
        return True if obj.deleted == "N" else False

    def get_ensembl_url(self, obj):
        """Return the correct ensembl domain"""
        if obj.accession.database == "ENSEMBL_FUNGI":
            return "http://fungi.ensembl.org"
        elif obj.accession.database == "ENSEMBL_METAZOA":
            return "http://metazoa.ensembl.org"
        elif obj.accession.database == "ENSEMBL_PLANTS":
            return "http://plants.ensembl.org"
        elif obj.accession.database == "ENSEMBL_PROTISTS":
            return "http://protists.ensembl.org"
        else:
            return None

    def get_ensembl_splice_variants(self, obj):
        if obj.db_id != 25:  # 25 = ENSEMBL
            return None

        return get_related_sequence(obj.accession_id, "isoform")

    def get_gencode_ensembl_url(self, obj):
        if obj.db_id != 47:  # 47 = ENSEMBL_GENCODE
            return None

        if obj.accession_id.startswith("GENCODE:"):
            transcript_id = obj.accession_id.split(":")[1]
        elif obj.accession_id.startswith("ENSMUST"):
            transcript_id = obj.accession_id
        else:
            transcript_id = None

        if transcript_id:
            species = obj.accession.species.replace(" ", "_")
            return f"http://ensembl.org/{species}/Transcript/Summary?t={transcript_id}"
        else:
            return None

    def get_gencode_transcript_id(self, obj):
        if obj.db_id != 47:  # 47 = ENSEMBL_GENCODE
            return None

        if obj.accession_id.startswith("GENCODE:"):
            return obj.accession_id.split(":")[1]
        elif obj.accession_id.startswith("ENSMUST"):
            return obj.accession_id
        else:
            return None

    def get_mirbase_mature_products(self, obj):
        if obj.db_id != 4:  # 4 = MIRBASE
            return None

        return get_related_sequence(obj.accession_id, "mature_product")

    def get_mirbase_precursor(self, obj):
        if obj.db_id != 4:  # 4 = MIRBASE
            return None

        return get_related_sequence(obj.accession_id, "precursor")

    def get_quickgo_hits(self, obj):
        """Return the number of annotations in QuickGO"""
        if obj.accession.database == "PSICQUIC":
            urs_taxid = obj.upi.upi + "_" + str(obj.taxid)
            try:
                response = requests.get(
                    f"https://www.ebi.ac.uk/QuickGO/services/annotation/stats?geneProductId={urs_taxid}"
                )
                data = json.loads(response.text)
                hits = data["results"][0]["totalHits"]
            except Exception:
                hits = None
        else:
            hits = None
        return hits

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
