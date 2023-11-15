from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from .serializers import BlogSerializer
from .models import Article


@extend_schema(exclude=True)
class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint to show blog posts"""

    queryset = Article.objects.all()
    serializer_class = BlogSerializer


@extend_schema(exclude=True)
class BlogFeaturedViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint to show featured blog posts"""

    queryset = Article.objects.filter(featured=True)
    serializer_class = BlogSerializer
