from rest_framework import filters, generics

from .serializers import XrefSerializer
from ...models import Xref


class XrefAPIViewSet(generics.ListAPIView):
    """
    List of cross-references for a particular RNA sequence in a specific species
    """
    serializer_class = XrefSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["db__display_name"]

    def get_queryset(self):
        upi = self.kwargs["upi"]
        try:
            taxid = self.kwargs["taxid"]
        except KeyError:
            taxid = None

        xrefs = Xref.objects.filter(deleted="N", upi=upi)\
            .exclude(accession__accession__startswith="PSICQUIC")\
            .order_by("-db__id")

        # Sometimes xrefs are deleted from databases (e.g. when by mistake they
        # were annotated as RNA being in fact protein-coding sequences). If our
        # xrefs list doesn't contain proper RNA sequences, we should at least
        # return these wrong annotations to hard-links to deleted sequences
        # accessible from web.
        if not xrefs:
            xrefs = Xref.objects.filter(deleted="Y", upi=upi)\
                .order_by("-db__id")

        if taxid:
            xrefs = xrefs.filter(taxid=taxid)

        return xrefs
