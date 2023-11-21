from rest_framework import generics

from .serializers import RfamHitsSerializer
from ...models import RfamHit
from ...utils import django_filter_warning


class RfamHitsViewSet(generics.ListAPIView):
    """API endpoint for interactions."""

    serializer_class = RfamHitsSerializer

    @django_filter_warning
    def get_queryset(self):
        upi = self.kwargs["upi"]
        return RfamHit.objects.filter(upi=upi).select_related("rfam_model", "rfam_model__rfam_clan_id")
