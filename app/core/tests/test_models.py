from django.test import TestCase
from core import models


class ModelTests(TestCase):
    def test_wedding_str(self):
        """Test the wedding string representation"""
        name = 'Bart'
        email = 'test@email.com'
        date = 'October 10th, 2022'
        image = 'smthg.jpg'
        wedding = models.Wedding.objects.create(
            name=name,
            email=email,
            date=date,
            image=image
        )

        self.assertEqual(str(wedding), wedding.name)
