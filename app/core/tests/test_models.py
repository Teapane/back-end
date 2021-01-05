from django.test import TestCase
from core import models


class ModelTests(TestCase):

    def setUp(self):
        self.wedding1 = models.Wedding.objects.create(
            name = 'Bart',
            email = 'test@email.com',
            date = 'October 10th, 2022',
            image = 'smthg.jpg'
        )


    def test_wedding_str(self):
        """Test the wedding string representation"""

        self.assertEqual(str(self.wedding1), self.wedding1.name)


    def test_guest_str(self):
        """Test the guest string representation"""
        name = 'Marge'
        phone_number = '1234567890'
        guest = models.Guest.objects.create(
            name=name,
            phone_number=phone_number,
            wedding=self.wedding1
        )

        self.assertEqual(str(guest), guest.name)
