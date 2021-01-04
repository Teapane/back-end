from django.test import TestCase
from core import models


class ModelTests(TestCase):
    def test_vendor_str(self):
        """Test the vendor string representation"""
        name = 'Bart'
        email = 'test@email.com'
        vendor = models.Vendor.objects.create(
            name=name
        )

        self.assertEqual(str(vendor), vendor.name)


    # def test_new_user_email_normalized(self):
    #     """Test the email for a new user is normalized"""
    #     email = 'test@EMAIL.com'
    #     user = get_user_model().objects.create_user(email, 'test123')
    #
    #     self.assertEqual(user.email, email.lower())
    #
    # def test_new_user_valid_email(self):
    #     """Test creating user with no email raises error"""
    #     with self.assertRaises(ValueError):
    #         get_user_model().objects.create_user(None, 'test123')
