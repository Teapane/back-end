from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Wedding
from core.models import Guest

CREATE_PHOTO_URL = reverse('wedding:create_photo')


class PostPhotoTests(TestCase):
    """Test module for POST photo API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_photo_success(self):
        """Test creating photo with valid credentials is successful"""

        wedding = Wedding(
                        name='Simpsons',
                        email='simpsonwed@gmail.com',
                        date='2345675432'
                        )
        wedding.save()

        guest = Guest.objects.create(
                        name='Uncle Bob',
                        phone_number='2343454567',
                        wedding=wedding
        )

        photo_data = {
            'number': '1',
            'description': 'Bride with Groom Family',
            'guest': guest.id
        }

        res = self.client.post(CREATE_PHOTO_URL, photo_data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
