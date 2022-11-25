from django.db import models


class EnsemblCompara(models.Model):
    id = models.IntegerField(primary_key=True)
    ensembl_transcript_id = models.TextField()
    urs_taxid = models.ForeignKey(
        "RnaPrecomputed",
        to_field="id",
        db_column="urs_taxid",
        on_delete=models.CASCADE
    )
    homology_id = models.IntegerField()

    class Meta:
        db_table = "ensembl_compara"
        ordering = ["ensembl_transcript_id"]

    def __str__(self):
        return self.id
