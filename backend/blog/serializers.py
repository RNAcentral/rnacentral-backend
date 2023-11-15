from rest_framework import serializers


class BlogSerializer(serializers.Serializer):
    """Serializer class for blog posts"""

    title = serializers.CharField()
    release_image = serializers.CharField()
    content = serializers.CharField()
    created = serializers.DateField(format="%Y-%m-%d")
    featured = serializers.BooleanField()
