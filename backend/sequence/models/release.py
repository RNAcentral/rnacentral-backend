from django.db import models


class Release(models.Model):
    db = models.ForeignKey(
        "Database", db_column="dbid", related_name="db", on_delete=models.CASCADE
    )
    release_date = models.DateField()
    release_type = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    timestamp = models.DateField()
    userstamp = models.CharField(max_length=30)
    descr = models.TextField()
    force_load = models.CharField(max_length=1)

    class Meta:
        db_table = "rnc_release"
        ordering = ["-release_date"]

    def __str__(self):
        return str(self.release_date)
