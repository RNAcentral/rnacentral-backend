from django.db import models


class Database(models.Model):
    timestamp = models.DateField()
    userstamp = models.CharField(max_length=30)
    descr = models.CharField(max_length=60)
    current_release = models.IntegerField()
    full_descr = models.CharField(max_length=255)
    alive = models.CharField(max_length=1)
    for_release = models.CharField(max_length=1)
    display_name = models.CharField(max_length=60)
    project_id = models.CharField(max_length=20)
    avg_length = models.BigIntegerField()
    min_length = models.BigIntegerField()
    max_length = models.BigIntegerField()
    num_sequences = models.BigIntegerField()
    num_organisms = models.BigIntegerField()

    class Meta:
        db_table = "rnc_database"

    def __str__(self):
        return self.display_name
