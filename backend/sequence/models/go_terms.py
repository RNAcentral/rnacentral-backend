from django.db.models import JSONField
from django.db import models


class OntologyTerm(models.Model):
    # An ontology term id is of the form: GO:0006617
    ontology_term_id = models.CharField(max_length=10, db_index=True, primary_key=True)
    ontology = models.CharField(max_length=5)
    name = models.TextField()
    definition = models.TextField()

    class Meta:
        db_table = "ontology_terms"
        ordering = ["ontology_term_id"]

    def __str__(self):
        return self.ontology_term_id

    def url(self):
        if self.ontology != "GO":
            return None
        return f"http://amigo.geneontology.org/amigo/term/{self.ontology_term_id}"

    def quickgo_url(self):
        if self.ontology != "GO":
            return None
        return f"https://www.ebi.ac.uk/QuickGO/term/{self.ontology_term_id}"


class GoAnnotation(models.Model):
    go_term_annotation_id = models.AutoField(primary_key=True)
    rna_id = models.CharField(max_length=50, null=False)
    qualifier = models.CharField(max_length=30, null=False)
    ontology_term = models.ForeignKey(
        "OntologyTerm",
        db_column="ontology_term_id",
        to_field="ontology_term_id",
        null=False,
        related_name="go_annotations",
        on_delete=models.CASCADE,
    )
    evidence_code = models.ForeignKey(
        "OntologyTerm",
        db_column="evidence_code",
        to_field="ontology_term_id",
        null=False,
        related_name="go_annotation_evidence",
        on_delete=models.CASCADE,
    )
    assigned_by = models.CharField(max_length=50)
    extensions = JSONField()

    class Meta:
        db_table = "go_term_annotations"
        ordering = ["qualifier"]

    def __str__(self):
        return self.go_term_annotation_id
