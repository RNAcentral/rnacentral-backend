from django.http import Http404
from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RnaSerializer, TaxonomySerializer
from ...models import RnaPrecomputed, Taxonomy


class RnaPrecomputedViewSet(APIView):
    """Unique RNAcentral Sequence"""

    def get_view_name(self):
        return "RNA"

    def get_object(self, pk):
        try:
            return RnaPrecomputed.objects.get(pk=pk)
        except RnaPrecomputed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rna = self.get_object(pk)
        serializer = RnaSerializer(rna)
        return Response(serializer.data)


class TaxonomyViewSet(generics.ListAPIView):
    """API to search the sequence in other species"""
    serializer_class = TaxonomySerializer

    def get_queryset(self):
        upi = self.kwargs["upi"]
        taxid = self.kwargs["taxid"]
        get_annotations_from_other_species = []

        rna_precomputed = RnaPrecomputed.objects.filter(
            ~Q(taxid=taxid), ~Q(taxid__isnull=True), upi=upi, is_active=True
        )

        for item in rna_precomputed:
            try:
                taxonomy = Taxonomy.objects.get(pk=item.taxid)
                get_annotations_from_other_species.append(
                    {
                        "urs_taxid": item.id,
                        "short_description": item.short_description,
                        "species_name": taxonomy.name
                    }
                )
            except Taxonomy.DoesNotExist:
                pass

        return get_annotations_from_other_species
