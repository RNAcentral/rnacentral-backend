from rest_framework import viewsets

from .serializers import QcStatusSerializer
from ...models import QcStatus


class QcStatusViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint showing the QC status for a sequence."""

    queryset = QcStatus.objects.all()
    serializer_class = QcStatusSerializer

    def get_view_name(self):
        return "QC Status"
