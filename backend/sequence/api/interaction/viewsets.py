from rest_framework import generics

from .serializers import InteractionsSerializer
from ...models import Interactions


class InteractionsViewSet(generics.ListAPIView):
    """API endpoint for interactions."""

    serializer_class = InteractionsSerializer

    def get_queryset(self):
        urs_taxid = self.kwargs["urs_taxid"]

        return Interactions.objects.filter(urs_taxid=urs_taxid)
