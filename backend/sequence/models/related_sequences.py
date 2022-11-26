from django.contrib.postgres.fields import ArrayField
from django.db import models


class RelatedSequence(models.Model):
    id = models.AutoField(primary_key=True)

    source_accession = models.CharField(max_length=50)
    source_urs_taxid = models.ForeignKey(
        "RnaPrecomputed",
        db_column="source_urs_taxid",
        to_field="id",
        null=True,
        related_name="related_sequence",
        on_delete=models.CASCADE,
    )

    # TODO: create FK?
    # target_accession = models.ForeignKey(
    #     "ProteinInfo",
    #     db_column="target_accession",
    #     to_field="protein_accession",
    #     related_name="protein_accession",
    #     on_delete=models.CASCADE,
    # )
    target_accession = models.CharField(max_length=50)
    target_urs_taxid = models.ForeignKey(
        "RnaPrecomputed",
        db_column="target_urs_taxid",
        to_field="id",
        null=True,
        on_delete=models.CASCADE,
    )
    relationship_type = models.TextField()
    methods = ArrayField(models.TextField(), null=True)

    class Meta:
        db_table = "rnc_related_sequences"
        ordering = ["target_accession"]

    def __str__(self):
        return self.target_accession
