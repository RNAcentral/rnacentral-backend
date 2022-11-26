from django.contrib.postgres.fields import ArrayField
from django.db import models


class ProteinInfo(models.Model):
    protein_accession = models.TextField(
        primary_key=True,
        db_column="protein_accession",
    )
    description = models.TextField()
    label = models.TextField(null=True)
    synonyms = ArrayField(models.TextField(), null=True)

    class Meta:
        db_table = "protein_info"
        ordering = ["protein_accession"]

    def __str__(self):
        return self.protein_accession
