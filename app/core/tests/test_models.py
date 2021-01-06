from django.test import TestCase
from core import models


class ModelTests(TestCase):

    def setUp(self):
        self.wedding1 = models.Wedding.objects.create(
            name='Bart',
            email='test@email.com',
            date='October 10th, 2022'
        )

        self.guest1 = models.Guest.objects.create(
            name='Marge',
            phone_number='1234567890',
            wedding=self.wedding1
        )

        self.photo1 = models.Photo.objects.create(
            number='1'
        )

        self.photoguest1 = models.PhotoGuest.objects.create(
            guest=self.guest1,
            photo=self.photo1
        )

        self.weddingguest1 = models.WeddingGuest.objects.create(
            wedding=self.wedding1,
            guest=self.guest1
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

    def test_photo_str(self):
        """Test the photo string representation"""
        self.assertEqual(str(self.photo1), self.photo1.number)

    def test_photoguest_attrs(self):
        """Test the photoguest attribute representations"""
        self.assertEqual((self.photoguest1.photo), self.photo1)
        self.assertEqual((self.photoguest1.guest), self.guest1)

    def test_wedding_guest_attrs(self):
        """Test the photoguest attribute representations"""
        self.assertEqual((self.weddingguest1.wedding), self.wedding1)
        self.assertEqual((self.weddingguest1.guest), self.guest1)
