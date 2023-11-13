from rest_framework import serializers


class AccessionSerializer(serializers.Serializer):
    """Serializer class for individual cross-references"""

    url = serializers.HyperlinkedIdentityField(
        view_name="accession-detail", read_only=True
    )
    id = serializers.CharField(source="accession")
    parent_ac = serializers.CharField()
    seq_version = serializers.IntegerField()
    feature_start = serializers.IntegerField()
    feature_end = serializers.IntegerField()
    description = serializers.CharField()
    external_id = serializers.CharField()
    optional_id = serializers.CharField()
    gene = serializers.CharField()
    species = serializers.CharField()
    organelle = serializers.CharField()
    classification = serializers.CharField()
    inference = serializers.CharField()
    locus_tag = serializers.CharField()
    note = serializers.CharField(source="get_json_object_from_note")
    standard_name = serializers.CharField()
    external_id_without_version = serializers.CharField(
        source="get_external_id_without_version"
    )
    pdb_entity_id = serializers.CharField(source="get_pdb_entity_id")
    ena_url = serializers.CharField(source="get_ena_url")
    ensembl_species_url = serializers.CharField(source="get_ensembl_species_url")
