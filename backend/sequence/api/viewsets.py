from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import SequenceFeatureSerializer
from ..models import SequenceFeature


class SequenceFeaturesAPIViewSet(generics.ListAPIView):
    """API endpoint with sequence features (CRS, mature miRNAs etc)"""
    permission_classes = [AllowAny]
    serializer_class = SequenceFeatureSerializer

    def get_queryset(self):
        upi = self.kwargs["upi"]
        taxid = self.kwargs["taxid"]

        return SequenceFeature.objects.filter(
            upi=upi,
            taxid=taxid,
            feature_name__in=["conserved_rna_structure", "mature_product", "cpat_orf"],
        )
