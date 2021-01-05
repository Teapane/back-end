from django.test import TestCase
from core import models


class ModelTests(TestCase):
    def test_vendor_str(self):
        """Test the vendor string representation"""
        name = 'Bart'
        vendor = models.Vendor.objects.create(
            name=name
        )

        self.assertEqual(str(vendor), vendor.name)
