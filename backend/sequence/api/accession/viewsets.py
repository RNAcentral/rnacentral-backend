from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AccessionSerializer
from ...models import Accession


class AccessionAPIViewSet(APIView):
    """API endpoint that allows single accessions to be viewed"""

    def get_object(self, pk):
        try:
            return Accession.objects.get(pk=pk)
        except Accession.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        accession = self.get_object(pk)
        serializer = AccessionSerializer(accession, context={"request": request})
        return Response(serializer.data)
