from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RnaSerializer
from ...models import Rna


class RnaAPIViewSet(APIView):
    """Unique RNAcentral Sequence"""

    def get_object(self, pk):
        try:
            return Rna.objects.get(pk=pk)
        except Rna.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rna = self.get_object(pk)
        serializer = RnaSerializer(rna)
        return Response(serializer.data)
