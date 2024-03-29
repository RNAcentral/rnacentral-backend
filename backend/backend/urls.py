"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from blog.views import BlogViewSet, BlogFeaturedViewSet
from sequence.api.accession.viewsets import AccessionViewSet
from sequence.api.sequence_feature.viewsets import SequenceFeaturesAPIViewSet
from sequence.api.rna_precomputed.viewsets import RnaPrecomputedViewSet, TaxonomyViewSet
from sequence.api.xref.viewsets import XrefAPIViewSet
from sequence.api.related_sequence.viewsets import (
    TargetLncRNAsViewSet,
    TargetMiRNAsViewSet,
    TargetProteinsViewSet,
)
from sequence.api.interaction.viewsets import InteractionsViewSet
from sequence.api.ensembl_compara.viewsets import EnsemblComparaViewSet
from sequence.api.go_terms.viewsets import GoTermsViewSet
from sequence.api.qc_status.viewsets import QcStatusViewSet
from sequence.api.rfam.viewsets import RfamHitsViewSet
from sequence.api.sequence_region.viewsets import SequenceRegionViewSet
from sequence.api.database.viewsets import DatabaseViewSet, DatabaseListViewSet
from sequence.api.secondary_structure.viewsets import SecondaryStructure

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path(
        # single RNAcentral sequence
        "api/v2/rna/<str:pk>",
        RnaPrecomputedViewSet.as_view(),
        name="rna-detail",
    ),
    path(
        # sequence features found in a sequence
        "api/v2/rna/<str:upi>/sequence-features/<int:taxid>",
        SequenceFeaturesAPIViewSet.as_view(),
        name="rna-sequence-features",
    ),
    path(
        # view for an individual cross-reference
        "api/v2/accession/<str:pk>",
        AccessionViewSet.as_view({"get": "retrieve"}),
        name="accession-detail",
    ),
    path(
        # view for all cross-references associated with
        # an RNAcentral id - no taxid
        "api/v2/rna/<str:upi>/xrefs",
        XrefAPIViewSet.as_view(),
        name="rna-xrefs",
    ),
    path(
        # view for all cross-references associated with
        # an RNAcentral id and taxid
        "api/v2/rna/<str:upi>/xrefs/<int:taxid>",
        XrefAPIViewSet.as_view(),
        name="rna-xrefs",
    ),
    path(
        # view for protein targets
        "api/v2/rna/<str:source_urs_taxid>/protein-targets",
        TargetProteinsViewSet.as_view(),
        name="protein-targets",
    ),
    path(
        # view for targeting lncRNAs
        "api/v2/rna/<str:source_urs_taxid>/lncrna-targets",
        TargetLncRNAsViewSet.as_view(),
        name="lncrna-targets",
    ),
    path(
        # view for targeting miRNAs
        "api/v2/rna/<str:target_urs_taxid>/mirna-targets",
        TargetMiRNAsViewSet.as_view(),
        name="mirna-targets",
    ),
    path(
        # view for interactions
        "api/v2/rna/<str:urs_taxid>/interactions",
        InteractionsViewSet.as_view(),
        name="interactions",
    ),
    path(
        # view for related RNAs in other species
        "api/v2/rna/<str:urs_taxid>/ensembl-compara",
        EnsemblComparaViewSet.as_view(),
        name="ensembl-compara",
    ),
    path(
        # view for gene ontology annotations
        "api/v2/rna/<str:rna_id>/go-annotations",
        GoTermsViewSet.as_view(),
        name="go-annotations",
    ),
    path(
        # information about the qc status for a given sequence
        "api/v2/rna/<str:pk>/qc-status",
        QcStatusViewSet.as_view({"get": "retrieve"}),
        name="qc-status",
    ),
    path(
        # rfam hits found in this RNAcentral id
        "api/v2/rna/<str:upi>/rfam-hits",
        RfamHitsViewSet.as_view(),
        name="rfam-hits",
    ),
    path(
        # genome locations for RNA (species-specific)
        "api/v2/rna/<str:urs_taxid>/genome-locations",
        SequenceRegionViewSet.as_view(),
        name="genome-locations",
    ),
    path(
        # search the sequence in other species
        "api/v2/rna/<str:upi>/taxonomy/<int:taxid>",
        TaxonomyViewSet.as_view(),
        name="taxonomy",
    ),
    path(
        # secondary structure thumbnail in SVG format
        "api/v2/rna/<str:upi>/2d/svg",
        SecondaryStructure.as_view(),
        name="rna-2d-svg",
    ),
    path(
        # list of Expert DB
        "api/v2/database",
        DatabaseListViewSet.as_view(),
        name="database-list",
    ),
    path(
        # view for specifc Expert DB
        "api/v2/database/<str:pk>",
        DatabaseViewSet.as_view(),
        name="database",
    ),
    path(
        # list of blog posts
        "blog",
        BlogViewSet.as_view({"get": "list"}),
        name="blog-list"
    ),
    path(
        # view specific post
        "blog/<int:pk>",
        BlogViewSet.as_view({"get": "retrieve"}),
        name="blog-detail"
    ),
    path(
        # list of featured blog posts
        "blog/highlight",
        BlogFeaturedViewSet.as_view({"get": "list"}),
        name="blog-featured"
    ),
    path("ckeditor/", include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
