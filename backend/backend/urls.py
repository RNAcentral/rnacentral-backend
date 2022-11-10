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
from django.urls import path

from sequence.api.accession.viewsets import AccessionAPIViewSet
from sequence.api.sequence_feature.viewsets import SequenceFeaturesAPIViewSet
from sequence.api.rna.viewsets import RnaAPIViewSet

urlpatterns = [
    path(
        # sequence features found in a sequence
        "api/v2/rna/<str:upi>/sequence-features/<int:taxid>",
        SequenceFeaturesAPIViewSet.as_view(),
        name="rna-sequence-features"
    ),
    path(
        # view for an individual cross-reference
        "api/v2/accession/<str:pk>/info",
        AccessionAPIViewSet.as_view(),
        name="accession-detail"
    ),
    path(
        # single RNAcentral sequence
        "api/v2/rna/<str:pk>",
        RnaAPIViewSet.as_view(),
        name="rna-detail"
    ),
]
