from django.db import models


class Xref(models.Model):
    id = models.AutoField(primary_key=True)
    db = models.ForeignKey(
        "Database", db_column="dbid", related_name="xrefs", on_delete=models.CASCADE
    )
    accession = models.OneToOneField(
        "Accession",
        db_column="ac",
        to_field="accession",
        related_name="xrefs",
        on_delete=models.CASCADE,
    )
    created = models.ForeignKey(
        "Release",
        db_column="created",
        related_name="release_created",
        on_delete=models.CASCADE,
    )
    last = models.ForeignKey(
        "Release",
        db_column="last",
        related_name="last_release",
        on_delete=models.CASCADE,
    )
    upi = models.ForeignKey(
        "Rna",
        db_column="upi",
        to_field="upi",
        related_name="xrefs",
        on_delete=models.CASCADE,
    )
    version_i = models.IntegerField()
    deleted = models.CharField(max_length=1)
    timestamp = models.DateTimeField()
    userstamp = models.CharField(max_length=100)
    version = models.IntegerField()
    taxid = models.IntegerField()

    class Meta:
        db_table = "xref"
        ordering = ["db"]

    def __str__(self):
        return self.upi
