from django.db import models


class Rna(models.Model):
    id = models.IntegerField(db_column="id")
    upi = models.CharField(max_length=13, db_index=True, primary_key=True)
    timestamp = models.DateTimeField()
    userstamp = models.CharField(max_length=30)
    crc64 = models.CharField(max_length=16)
    length = models.IntegerField(db_column="len")
    seq_short = models.CharField(max_length=4000)
    seq_long = models.TextField()
    md5 = models.CharField(max_length=32, unique=True, db_index=True)

    class Meta:
        db_table = "rna"
        ordering = ["-upi"]

    def __str__(self):
        return self.upi

    def get_sequence(self):
        """
        Sequences of up to 4000 nucleotides are stored in seq_short, while the
        longer ones are in stored in seq_long.
        This was due to Oracle column size restrictions.
        """
        if self.seq_short:
            sequence = self.seq_short
        else:
            sequence = self.seq_long
        return sequence.replace("T", "U").upper()
