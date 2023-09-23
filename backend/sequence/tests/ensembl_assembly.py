from rest_framework import serializers
from rest_framework.test import APITestCase

from ..api.ensembl_assembly.serializers import EnsemblAssemblySerializer


class EnsemblAssemblySerializerTest(APITestCase):
    def test_serializer_fields(self):
        serializer = EnsemblAssemblySerializer()
        expected_fields = {
            "assembly_id": serializers.ReadOnlyField,
            "species": serializers.ReadOnlyField,
            "ucsc_db_id": serializers.ReadOnlyField,
            "ensembl_division_name": serializers.ReadOnlyField,
            "ensembl_division_url": serializers.SerializerMethodField,
            "ensembl_species_url": serializers.ReadOnlyField,
        }

        # Check if the serializer has the expected fields
        for field_name, field_instance in expected_fields.items():
            self.assertTrue(field_name in serializer.fields)
            self.assertIsInstance(serializer.fields[field_name], field_instance)
