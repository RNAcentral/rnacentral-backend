from django.db import models


class EnsemblAssembly(models.Model):
    assembly_id = models.CharField(primary_key=True, max_length=255)
    assembly_full_name = models.CharField(max_length=255, db_index=True)
    gca_accession = models.CharField(max_length=20, db_index=True, null=True)
    assembly_ucsc = models.CharField(max_length=100, db_index=True, null=True)
    common_name = models.CharField(max_length=255, db_index=True, null=True)
    taxid = models.IntegerField(unique=True)  # unique creates an index
    ensembl_url = models.CharField(max_length=100, db_index=True, null=True)
    division = models.CharField(max_length=20, db_index=True, null=True)
    subdomain = models.CharField(max_length=100, db_index=True, default="ensembl.org")
    example_chromosome = models.CharField(max_length=20, null=True)
    example_start = models.IntegerField(null=True)
    example_end = models.IntegerField(null=True)

    class Meta:
        db_table = "ensembl_assembly"
        ordering = ["assembly_full_name"]

    def __str__(self):
        return self.assembly_full_name

    @property
    def get_human_readable_ensembl_url(self):
        return self.ensembl_url.replace("_", " ").capitalize()
