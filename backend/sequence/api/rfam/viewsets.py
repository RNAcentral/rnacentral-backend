from rest_framework import generics

from .serializers import RfamHitsSerializer
from ...models import RfamHit


class RfamHitsViewSet(generics.ListAPIView):
    """API endpoint for interactions."""

    serializer_class = RfamHitsSerializer

    def get_queryset(self):
        upi = self.kwargs["upi"]
        return RfamHit.objects.filter(upi=upi).select_related("rfam_model")
