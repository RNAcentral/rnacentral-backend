from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .serializers import InteractionsSerializer
from ...models import Interactions
from ...utils import django_filter_warning


@extend_schema(request=None, responses=InteractionsSerializer)
class InteractionsViewSet(generics.ListAPIView):
    """API endpoint for interactions."""

    serializer_class = InteractionsSerializer

    @django_filter_warning
    def get_queryset(self):
        urs_taxid = self.kwargs["urs_taxid"]

        return Interactions.objects.filter(urs_taxid=urs_taxid)
