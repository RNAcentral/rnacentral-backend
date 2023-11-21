from rest_framework import generics

from .serializers import SequenceFeatureSerializer
from ...models import SequenceFeature
from ...utils import django_filter_warning


class SequenceFeaturesAPIViewSet(generics.ListAPIView):
    """API endpoint with sequence features (CRS, mature miRNAs etc)"""

    serializer_class = SequenceFeatureSerializer

    @django_filter_warning
    def get_queryset(self):
        upi = self.kwargs["upi"]
        taxid = self.kwargs["taxid"]

        return SequenceFeature.objects.filter(upi=upi, taxid=taxid).select_related("upi")
