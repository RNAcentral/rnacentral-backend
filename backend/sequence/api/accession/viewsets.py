from rest_framework import viewsets

from .serializers import AccessionSerializer
from ...models import Accession


class AccessionViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows single accessions to be viewed"""

    queryset = Accession.objects.all()
    serializer_class = AccessionSerializer
