import re

from rest_framework import serializers


class InteractionsSerializer(serializers.Serializer):
    """Serializer class for interactions"""

    intact_id = serializers.ReadOnlyField()
    intact_id_url = serializers.SerializerMethodField(method_name="get_intact_id_url")
    interacting_id = serializers.SerializerMethodField(method_name="get_interacting_id")
    interacting_id_url = serializers.SerializerMethodField(
        method_name="get_interacting_id_url"
    )
    names = serializers.JSONField(read_only=True)

    def get_intact_id_url(self, obj):
        match = re.search(r"URS[0-9A-Fa-f]{10}[_-]\d+", obj.intact_id)
        return (
            None
            if match
            else f"https://www.ebi.ac.uk/intact/interaction/{obj.intact_id}"
        )

    def get_interacting_id(self, obj):
        match = re.search(r"URS[0-9A-Fa-f]{10}[_-]\d+", "".join(obj.names))
        if match:
            interacting_id = match.group()
        elif "uniprotkb:" in obj.interacting_id:
            interacting_id = obj.interacting_id.replace("uniprotkb:", "")
        else:
            interacting_id = obj.interacting_id
        return interacting_id

    def get_interacting_id_url(self, obj):
        match = re.search(r"URS[0-9A-Fa-f]{10}[_-]\d+", "".join(obj.names))
        if match:
            url = "/rna/" + match.group()
        elif "uniprotkb:" in obj.interacting_id:
            uniprot_id = obj.interacting_id.replace("uniprotkb:", "")
            url = "https://www.uniprot.org/uniprot/" + uniprot_id
        else:
            url = None
        return url
