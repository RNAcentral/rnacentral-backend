from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .serializers import GoTermsSerializer
from ...models import GoAnnotation
from ...utils import django_filter_warning


@extend_schema(request=None, responses=GoTermsSerializer)
class GoTermsViewSet(generics.ListAPIView):
    """API endpoint for GO terms."""

    serializer_class = GoTermsSerializer

    def get_view_name(self):
        return "Gene Ontology annotations"

    @django_filter_warning
    def get_queryset(self):
        rna_id = self.kwargs["rna_id"]

        return GoAnnotation.objects.filter(rna_id=rna_id).select_related(
            "ontology_term", "evidence_code"
        )
