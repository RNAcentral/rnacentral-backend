from rest_framework import generics

from .serializers import EnsemblComparaSerializer
from ...models import EnsemblCompara


class EnsemblComparaViewSet(generics.ListAPIView):
    """API endpoint for related sequences identified by Ensembl Compara."""
    serializer_class = EnsemblComparaSerializer

    def get_queryset(self):
        urs_taxid = self.kwargs["urs_taxid"]
        homology_id = EnsemblCompara.objects.filter(
            urs_taxid__id=urs_taxid
        ).first()

        if homology_id:
            return EnsemblCompara.objects.filter(
                homology_id=homology_id.homology_id).\
                exclude(urs_taxid=urs_taxid).\
                order_by("urs_taxid__description")
        else:
            return []
