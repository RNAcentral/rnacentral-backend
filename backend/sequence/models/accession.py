from django.db import models


class Accession(models.Model):
    accession = models.CharField(max_length=100, primary_key=True)

    # in miRNAs mature products and precursor have the same parent_ac
    parent_ac = models.CharField(max_length=100)

    seq_version = models.IntegerField(db_index=True)
    feature_start = models.IntegerField(db_index=True)
    feature_end = models.IntegerField(db_index=True)

    # INSDC classification; 'ncRNA', unless it's rRNA/tRNA/precursor RNA
    feature_name = models.CharField(max_length=20)

    ordinal = models.IntegerField()
    division = models.CharField(max_length=3)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    species = models.CharField(max_length=150)
    organelle = models.CharField(max_length=100)
    classification = models.CharField(max_length=500)
    project = models.CharField(max_length=50)
    is_composite = models.CharField(max_length=1)
    non_coding_id = models.CharField(max_length=100)
    database = models.CharField(max_length=20)
    external_id = models.CharField(max_length=150)

    # GeneID (without coordinates); used to find splice variants for lncRNAs OR mature/precursor RNAs for miRNAs
    optional_id = models.CharField(max_length=100)
    common_name = models.CharField(max_length=200, default="")

    anticodon = models.CharField(max_length=50)
    experiment = models.CharField(max_length=500)
    function = models.CharField(max_length=500)
    gene = models.CharField(max_length=50)
    gene_synonym = models.CharField(max_length=400)
    inference = models.CharField(max_length=100)
    locus_tag = models.CharField(max_length=50)
    genome_position = models.CharField(max_length=200, db_column="map")
    mol_type = models.CharField(max_length=50)
    ncrna_class = models.CharField(max_length=50)
    note = models.CharField(max_length=1600)
    old_locus_tag = models.CharField(max_length=50)
    product = models.CharField(max_length=300)
    db_xref = models.CharField(max_length=800)
    standard_name = models.CharField(max_length=100, default="")

    class Meta:
        db_table = "rnc_accessions"
