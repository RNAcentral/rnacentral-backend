from django.db import models

from .go_terms import OntologyTerm


class RfamClan(models.Model):
    """
    A simple container to store information about Rfam clans. This is just to
    contain some useful meta data about clans for display in RNAcentral.
    """

    rfam_clan_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    family_count = models.PositiveIntegerField()

    class Meta:
        db_table = "rfam_clans"
        ordering = ["rfam_clan_id"]

    def __str__(self):
        return self.name


class RfamModel(models.Model):
    """
    A simple container about Rfam families. This table contains just enough
    data to make it easy to display Rfam family data in RNAcentral.
    """

    rfam_model_id = models.CharField(max_length=20, primary_key=True)
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, null=True)
    rfam_clan_id = models.ForeignKey(
        RfamClan,
        db_column="rfam_clan_id",
        to_field="rfam_clan_id",
        null=True,
        on_delete=models.CASCADE,
    )

    seed_count = models.PositiveIntegerField()
    full_count = models.PositiveIntegerField()
    length = models.PositiveIntegerField()
    is_suppressed = models.BooleanField(default=False)
    domain = models.CharField(max_length=50, null=True)
    rna_type = models.CharField(max_length=250)
    rfam_rna_type = models.TextField()

    class Meta:
        db_table = "rfam_models"
        ordering = ["rfam_model_id"]

    def __str__(self):
        return self.rfam_model_id

    @property
    def url(self):
        return f"http://rfam.org/family/{self.rfam_model_id}"

    @property
    def thumbnail_url(self):
        return f"http://rfam.org/family/{self.rfam_model_id}/thumbnail"

    def go_terms(self):
        terms = []
        mapping = RfamGoTerm.objects.select_related("go_term").filter(
            rfam_model_id=self.rfam_model_id
        )
        for result in mapping.all():
            terms.append(result.go_term)

        return terms


class RfamHit(models.Model):
    """
    This represents a hit of an Rfam model against a particular sequence. The
    idea is that we represent the regions of the sequence and model that are
    matched.
    """

    rfam_hit_id = models.AutoField(primary_key=True)
    upi = models.ForeignKey(
        "Rna", db_column="upi", to_field="upi", on_delete=models.CASCADE
    )
    sequence_start = models.PositiveIntegerField()
    sequence_stop = models.PositiveIntegerField()
    sequence_completeness = models.FloatField()

    rfam_model = models.ForeignKey(
        RfamModel,
        db_column="rfam_model_id",
        to_field="rfam_model_id",
        on_delete=models.CASCADE,
    )
    model_start = models.PositiveIntegerField()
    model_stop = models.PositiveIntegerField()
    model_completeness = models.FloatField()

    overlap = models.CharField(max_length=30)
    e_value = models.FloatField()
    score = models.FloatField()

    class Meta:
        db_table = "rfam_model_hits"
        ordering = ["rfam_hit_id"]

    def __str__(self):
        return self.rfam_hit_id

    @property
    def rfam_clan_id(self):
        return self.rfam_model.rfam_clan_id


class RfamGoTerm(models.Model):
    rfam_go_term_id = models.AutoField(primary_key=True)
    go_term = models.ForeignKey(
        OntologyTerm,
        db_column="ontology_term_id",
        to_field="ontology_term_id",
        related_name="go_term",
        on_delete=models.CASCADE,
    )
    rfam_model = models.ForeignKey(
        RfamModel,
        db_column="rfam_model_id",
        to_field="rfam_model_id",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "rfam_go_terms"
        ordering = ["rfam_go_term_id"]
        unique_together = (("rfam_model", "go_term"),)

    def __str__(self):
        return self.rfam_go_term_id
