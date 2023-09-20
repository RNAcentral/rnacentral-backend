from rest_framework import serializers


class AccessionSerializer(serializers.Serializer):
    """Serializer class for individual cross-references"""

    url = serializers.HyperlinkedIdentityField(
        view_name="accession-detail", read_only=True
    )
    id = serializers.ReadOnlyField(source="accession")
    parent_ac = serializers.ReadOnlyField()
    seq_version = serializers.ReadOnlyField()
    feature_start = serializers.ReadOnlyField()
    feature_end = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    external_id = serializers.ReadOnlyField()
    optional_id = serializers.ReadOnlyField()
    gene = serializers.ReadOnlyField()
    species = serializers.ReadOnlyField()
    organelle = serializers.ReadOnlyField()
    classification = serializers.ReadOnlyField()
    inference = serializers.ReadOnlyField()
    locus_tag = serializers.ReadOnlyField()
    note = serializers.ReadOnlyField(source="get_json_object_from_note")
    standard_name = serializers.ReadOnlyField()
    external_id_without_version = serializers.ReadOnlyField(
        source="get_external_id_without_version"
    )
    pdb_entity_id = serializers.ReadOnlyField(source="get_pdb_entity_id")
    ena_url = serializers.ReadOnlyField(source="get_ena_url")
    ensembl_species_url = serializers.ReadOnlyField(source="get_ensembl_species_url")
