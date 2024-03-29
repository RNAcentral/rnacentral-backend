from django.db import models


class Database(models.Model):
    timestamp = models.DateField()
    userstamp = models.CharField(max_length=30)
    descr = models.CharField(max_length=60)
    current_release = models.IntegerField()
    full_descr = models.CharField(max_length=255)
    alive = models.CharField(max_length=1)
    for_release = models.CharField(max_length=1, blank=True)
    display_name = models.CharField(max_length=60)
    project_id = models.CharField(max_length=20, blank=True)
    avg_length = models.BigIntegerField(blank=True)
    min_length = models.BigIntegerField(blank=True)
    max_length = models.BigIntegerField(blank=True)
    num_sequences = models.BigIntegerField()
    num_organisms = models.BigIntegerField()
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    example = models.JSONField()
    reference = models.JSONField()

    class Meta:
        db_table = "rnc_database"
        ordering = ["display_name"]

    def __str__(self):
        return self.display_name
