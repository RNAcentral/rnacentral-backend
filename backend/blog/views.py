from rest_framework import viewsets

from .serializers import BlogSerializer
from .models import Article


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint to show blog posts"""

    queryset = Article.objects.all()
    serializer_class = BlogSerializer


class BlogFeaturedViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint to show featured blog posts"""

    queryset = Article.objects.filter(featured=True)
    serializer_class = BlogSerializer
