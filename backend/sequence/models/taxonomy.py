from django.db import models


class Taxonomy(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    lineage = models.TextField()
    aliases = models.TextField()
    replaced_by = models.ForeignKey(
        "self", db_column="replaced_by", on_delete=models.CASCADE
    )
    common_name = models.TextField()
    is_deleted = models.BooleanField()

    class Meta:
        db_table = "rnc_taxonomy"
        ordering = ["id"]

    def __str__(self):
        return self.name
