from django.db import models


class RnaPrecomputed(models.Model):
    """
    Contains 2 types of entries: species-specific (taxid != Null) and non-species-specific (taxid == Null).

    For every Rna there should be 1 entry in RnaPrecomputed, where taxid = Null and some species-specific.
    """

    id = models.CharField(
        max_length=44, primary_key=True
    )  # id = upi + taxid if taxid != Null else upi
    taxid = models.IntegerField(db_index=True, null=True)
    description = models.CharField(max_length=250, null=True)
    upi = models.ForeignKey(
        "Rna",
        db_column="upi",
        to_field="upi",
        related_name="precomputed",
        on_delete=models.CASCADE,
    )
    rna_type = models.CharField(max_length=250, null=True)
    update_date = models.DateField(auto_now=True)
    has_coordinates = models.BooleanField()
    databases = models.TextField(null=True)
    is_active = models.BooleanField()
    last_release = models.IntegerField(null=True)
    short_description = models.CharField(max_length=250)

    class Meta:
        db_table = "rnc_rna_precomputed"
        ordering = ["id"]

    def __str__(self):
        return self.id

    def get_databases(self):
        return self.databases.split(",") if self.databases else None

    def get_sequence(self):
        return self.upi.get_sequence()
