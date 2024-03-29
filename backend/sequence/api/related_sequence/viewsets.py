from rest_framework import generics

from .serializers import (
    TargetLncRNAsSerializer,
    TargetMiRNAsSerializer,
    TargetProteinsSerializer,
)
from ...models import RelatedSequence
from ...utils import django_filter_warning


class TargetLncRNAsViewSet(generics.ListAPIView):
    """API endpoint for target lncRNAs."""

    serializer_class = TargetLncRNAsSerializer

    def get_view_name(self):
        return "Target lncRNAs"

    @django_filter_warning
    def get_queryset(self):
        source_urs_taxid = self.kwargs["source_urs_taxid"]

        return RelatedSequence.objects.filter(
            relationship_type="target_rna",
            source_urs_taxid=source_urs_taxid,
        ).select_related("target_urs_taxid").order_by("target_urs_taxid")


class TargetMiRNAsViewSet(generics.ListAPIView):
    """API endpoint for target miRNAs."""

    serializer_class = TargetMiRNAsSerializer

    def get_view_name(self):
        return "Target MiRNAs"

    @django_filter_warning
    def get_queryset(self):
        target_urs_taxid = self.kwargs["target_urs_taxid"]

        return (RelatedSequence.objects.filter(
            relationship_type="target_rna",
            target_urs_taxid=target_urs_taxid,
        ).select_related("source_urs_taxid").order_by("source_urs_taxid__short_description"))


class TargetProteinsViewSet(generics.ListAPIView):
    """API endpoint for target proteins."""

    serializer_class = TargetProteinsSerializer

    @django_filter_warning
    def get_queryset(self):
        source_urs_taxid = self.kwargs["source_urs_taxid"]

        return RelatedSequence.objects.filter(
            relationship_type="target_protein",
            source_urs_taxid=source_urs_taxid,
        )
        # .select_related("target_accession")
