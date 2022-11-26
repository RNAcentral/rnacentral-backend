from rest_framework import generics

from .serializers import SequenceRegionSerializer
from ...models import RnaPrecomputed, SequenceRegion


class SequenceRegionViewSet(generics.ListAPIView):
    """
    List of distinct genomic locations, where a specific RNA is found in a specific species, extracted from xrefs.
    """
    serializer_class = SequenceRegionSerializer

    def get_queryset(self):
        urs_taxid = self.kwargs["urs_taxid"]

        # do not show genome coordinates for obsolete sequences
        try:
            rna_precomputed = RnaPrecomputed.objects.get(id=urs_taxid, is_active=True)
        except RnaPrecomputed.DoesNotExist:
            return SequenceRegion.objects.none()

        return SequenceRegion.objects.filter(urs_taxid=rna_precomputed).select_related("assembly")
