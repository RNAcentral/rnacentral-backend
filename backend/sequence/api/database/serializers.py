from rest_framework import serializers


class DatabaseListSerializer(serializers.Serializer):
    """Serializer class for a list of Expert Databases"""

    id = serializers.ReadOnlyField()
    descr = serializers.SerializerMethodField(method_name="get_descr")
    display_name = serializers.ReadOnlyField()
    url = serializers.ReadOnlyField()

    def get_descr(self, obj):
        return obj.descr.lower()


class DatabaseSerializer(serializers.Serializer):
    """Serializer class for an Expert Database"""

    id = serializers.ReadOnlyField()
    descr = serializers.ReadOnlyField()
    current_release = serializers.ReadOnlyField()
    full_descr = serializers.ReadOnlyField()
    alive = serializers.ReadOnlyField()
    display_name = serializers.ReadOnlyField()
    avg_length = serializers.ReadOnlyField()
    min_length = serializers.ReadOnlyField()
    max_length = serializers.ReadOnlyField()
    num_sequences = serializers.ReadOnlyField()
    num_organisms = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    url = serializers.ReadOnlyField()
    example = serializers.ReadOnlyField()
    reference = serializers.ReadOnlyField()
