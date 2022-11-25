from django.db import models
from django.db.models import JSONField


class QcStatus(models.Model):
    id = models.OneToOneField(
        "RnaPrecomputed",
        primary_key=True,
        db_column="rna_id",
        to_field="id",
        related_name="qc_status",
        on_delete=models.CASCADE,
    )
    upi = models.ForeignKey(
        "Rna",
        db_column="upi",
        to_field="upi",
        related_name="qc_statuses",
        on_delete=models.CASCADE,
    )
    taxid = models.IntegerField()
    has_issue = models.BooleanField()
    incomplete_sequence = models.BooleanField()
    possible_contamination = models.BooleanField()
    missing_rfam_match = models.BooleanField()
    from_repetitive_region = models.BooleanField()
    possible_orf = models.BooleanField()
    messages = JSONField()

    class Meta:
        db_table = "qa_status"
        ordering = ["id"]

    def __str__(self):
        return self.has_issue
