from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import QcStatusSerializer
from ...models import QcStatus


class QcStatusViewSet(APIView):
    """API endpoint showing the QC status for a sequence."""

    def get_view_name(self):
        return "QC Status"

    def get_object(self, pk):
        try:
            return QcStatus.objects.get(pk=pk)
        except QcStatus.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        status = self.get_object(pk)
        serializer = QcStatusSerializer(status)
        return Response(serializer.data)
