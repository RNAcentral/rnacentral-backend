import json
import re

from django.db import models


class Accession(models.Model):
    accession = models.CharField(max_length=100, primary_key=True)

    # in miRNAs mature products and precursor have the same parent_ac
    parent_ac = models.CharField(max_length=100)

    seq_version = models.IntegerField(db_index=True)
    feature_start = models.IntegerField(db_index=True)
    feature_end = models.IntegerField(db_index=True)

    # INSDC classification; 'ncRNA', unless it's rRNA/tRNA/precursor RNA
    feature_name = models.CharField(max_length=20)

    ordinal = models.IntegerField()
    division = models.CharField(max_length=3)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    species = models.CharField(max_length=150)
    organelle = models.CharField(max_length=100)
    classification = models.CharField(max_length=500)
    project = models.CharField(max_length=50)
    is_composite = models.CharField(max_length=1)
    non_coding_id = models.CharField(max_length=100)
    database = models.CharField(max_length=20)
    external_id = models.CharField(max_length=150)

    # GeneID (without coordinates); used to find splice variants for lncRNAs OR
    # mature/precursor RNAs for miRNAs
    optional_id = models.CharField(max_length=100)
    common_name = models.CharField(max_length=200, default="")

    anticodon = models.CharField(max_length=50)
    experiment = models.CharField(max_length=500)
    function = models.CharField(max_length=500)
    gene = models.CharField(max_length=50)
    gene_synonym = models.CharField(max_length=400)
    inference = models.CharField(max_length=100)
    locus_tag = models.CharField(max_length=50)
    genome_position = models.CharField(max_length=200, db_column="map")
    mol_type = models.CharField(max_length=50)
    ncrna_class = models.CharField(max_length=50)
    note = models.CharField(max_length=1600)
    old_locus_tag = models.CharField(max_length=50)
    product = models.CharField(max_length=300)
    db_xref = models.CharField(max_length=800)
    standard_name = models.CharField(max_length=100, default="")

    class Meta:
        db_table = "rnc_accessions"
        ordering = ["accession"]

    def __str__(self):
        return self.accession

    @property
    def get_external_id_without_version(self):
        """
        Some databases add version to id, e.g. Meth.acet._AE010299.1 from SRPDB.
        We want to remove the ".1" from the external_id
        """
        return re.sub("\.\d+$", "", self.external_id) if self.external_id else None

    @property
    def get_json_object_from_note(self):
        try:
            json_object = json.loads(self.note)
        except ValueError:
            json_object = ""
        return json_object

    @property
    def get_pdb_entity_id(self):
        """Example PDB accession: 1J5E_A_1 (PDB id, chain, entity id)"""
        return self.accession.split("_")[-1] if self.database == "PDBE" else None

    @property
    def get_ena_url(self):
        """
        Get the ENA entry url that refers to the entry from
        the Non-coding product containing the cross-reference.
        """
        # no ENA source links for these entries
        no_ena_links = [
            "RFAM",
            "PDBE",
            "REFSEQ",
            "RDP",
            "GtRNAdb",
            "lncRNAdb",
            "miRBase",
            "pombase",
            "Dictybase",
            "SGD",
            "snopy",
            "Srpdb",
            "tair",
            "tmRNA website",
        ]

        if self.database in no_ena_links:
            return ""

        ena_base_url = "https://www.ebi.ac.uk/ena/browser/view/Non-coding:"

        if self.is_composite == "Y":
            return ena_base_url + self.non_coding_id
        else:
            return ena_base_url + self.accession

    @property
    def get_ensembl_species_url(self):
        """Get species name in a format that can be used in Ensembl urls."""
        from .ensembl_assembly import EnsemblAssembly
        from .xref import Xref

        if "ENSEMBL" not in self.database:
            return ""

        if self.species == "Dictyostelium discoideum":
            species = "Dictyostelium discoideum AX4"
        elif self.species.startswith("Mus musculus") and self.accession.startswith(
            "MGP"
        ):  # Ensembl mouse strain
            parts = self.accession.split("_")

            if len(parts) == 3:
                species = "Mus musculus " + parts[1]
            else:
                species = self.species
        elif self.species.count(" ") > 1 or self.species.count("-") > 0:
            try:
                xref = Xref.objects.filter(
                    accession__accession=self.accession, deleted="N"
                ).get()
                ensembl_genome = EnsemblAssembly.objects.filter(
                    taxid=xref.taxid
                ).first()

                if ensembl_genome:
                    return ensembl_genome.ensembl_url
                else:
                    species = self.species
            except Xref.DoesNotExist:
                return None
            except EnsemblAssembly.DoesNotExist:
                return None
            except Exception:
                return None
        else:
            species = self.species

        return species.replace(" ", "_").lower()
