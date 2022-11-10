from django.db import models
from django.db.models import JSONField


class SequenceFeature(models.Model):
    id = models.AutoField(primary_key=True, db_column="rnc_sequence_features_id")
    accession = models.OneToOneField(
        "Accession",
        db_column="accession",
        to_field="accession",
        related_name="sequence_features",
        null=True,
        on_delete=models.CASCADE,
    )
    feature_name = models.CharField(max_length=50)
    metadata = JSONField()
    start = models.IntegerField()
    stop = models.IntegerField()
    taxid = models.IntegerField()
    upi = models.ForeignKey(
        "Rna",
        db_column="upi",
        to_field="upi",
        related_name="sequence_features",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "rnc_sequence_features"
        ordering = ["-id"]

    def __str__(self):
        return self.feature_name
