from django.http import Http404
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DatabaseSerializer, DatabaseListSerializer
from ...models import Database


@extend_schema(request=None, responses=DatabaseListSerializer)
class DatabaseListViewSet(generics.ListAPIView):
    """API endpoint for getting a list of Expert Databases"""

    serializer_class = DatabaseListSerializer

    def get_queryset(self):
        return Database.objects.filter(alive="Y")


@extend_schema(request=None, responses=DatabaseSerializer)
class DatabaseViewSet(APIView):
    """Get data from a specific Expert Database"""

    def get_object(self, pk):
        try:
            return Database.objects.get(pk=pk)
        except Database.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        database = self.get_object(pk)
        serializer = DatabaseSerializer(database)
        return Response(serializer.data)
