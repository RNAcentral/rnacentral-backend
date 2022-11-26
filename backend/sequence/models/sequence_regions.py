from django.contrib.postgres.fields import ArrayField
from django.db import models


class SequenceRegion(models.Model):
    id = models.AutoField(primary_key=True)
    urs_taxid = models.ForeignKey(
        "RnaPrecomputed",
        related_name="regions",
        db_column="urs_taxid",
        to_field="id",
        on_delete=models.CASCADE,
    )
    region_name = models.TextField()
    chromosome = models.TextField()
    strand = models.IntegerField()
    region_start = models.IntegerField()
    region_stop = models.IntegerField()
    assembly = models.ForeignKey(
        "EnsemblAssembly",
        related_name="regions",
        db_column="assembly_id",
        to_field="assembly_id",
        on_delete=models.CASCADE,
    )
    was_mapped = models.BooleanField()
    identity = models.IntegerField()
    providing_databases = ArrayField(models.TextField())
    exon_count = models.IntegerField()

    class Meta:
        db_table = "rnc_sequence_regions"
        ordering = ["region_name"]

    def __str__(self):
        return self.region_name
