from django.http import Http404
from django.db import connection
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RnaSerializer, TaxonomySerializer
from ...models import RnaPrecomputed
from ...utils import dictfetchall, django_filter_warning


@extend_schema(request=None, responses=RnaSerializer)
class RnaPrecomputedViewSet(APIView):
    """Unique RNAcentral Sequence"""

    def get_view_name(self):
        return "RNA"

    def get_object(self, pk):
        try:
            return (
                RnaPrecomputed.objects
                .select_related("upi")
                .only("id", "description", "rna_type", "databases",
                      "upi__seq_short", "upi__seq_long", "upi__length",
                      "upi__md5")
                .get(pk=pk))
        except RnaPrecomputed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rna = self.get_object(pk)
        serializer = RnaSerializer(rna)
        return Response(serializer.data)


class TaxonomyViewSet(generics.ListAPIView):
    """API to search the sequence in other species"""

    serializer_class = TaxonomySerializer

    @django_filter_warning
    def get_queryset(self):
        upi = self.kwargs["upi"]
        taxid = self.kwargs["taxid"]

        query = """
            SELECT t1.id AS urs_taxid, t1.short_description, t2.name as species_name
            FROM {rna_precomputed} t1, rnc_taxonomy t2
            WHERE t1.upi = '{urs}'
            AND t1.taxid != {taxid}
            AND t1.is_active is True
            AND t1.taxid is not NULL
            AND t1.taxid = t2.id
            ORDER BY description
            LIMIT 10000
        """.format(
            urs=upi, taxid=taxid, rna_precomputed=RnaPrecomputed._meta.db_table
        )
        with connection.cursor() as cursor:
            cursor.execute(query)
            data = dictfetchall(cursor)
        return data
