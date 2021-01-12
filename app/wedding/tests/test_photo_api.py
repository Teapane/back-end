from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Wedding
from core.models import Guest
from core.models import Photo


CREATE_PHOTO_URL = reverse('wedding:create_photo')


class PhotoTests(TestCase):
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
                        phoneNumber='2343454567',
                        wedding=wedding
        )

        photo_data = {
            'number': 1,
            'description': 'Bride with Groom Family',
            'guest': guest.id,
            'weddingId': wedding.id
        }

        res = self.client.post(CREATE_PHOTO_URL, photo_data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_get_all_photos_given_wedding_id(self):
        wedding1 = Wedding(
                        name='Simpsons',
                        email='simpsonwed@gmail.com',
                        date='2345675432'
                        )
        wedding1.save()

        wedding2 = Wedding.objects.create(
            name='Bart',
            email='test@email.com',
            date='October 10th, 2022'
        )

        guest1 = Guest.objects.create(
                        name='Uncle Bob',
                        phoneNumber='2343454567',
                        wedding=wedding1
        )

        guest2 = Guest.objects.create(
            name='Aunt Joan',
            phoneNumber='3450962384',
            wedding=wedding1
        )

        guest3 = Guest.objects.create(
            name='Grandma Charlotte',
            phoneNumber='34523462384',
            wedding=wedding2
        )

        photo1 = Photo.objects.create(
                        number=5,
                        description="Bride's family",
                        weddingId=wedding1
        )

        photo1.guest.set([guest1, guest2])

        photo2 = Photo.objects.create(
                        number=6,
                        description="Friends",
                        weddingId=wedding2
        )

        photo2.guest.set([guest3])

        res = self.client.get(
                    "/api/v1/weddings/photos/?weddingId=% s" % wedding1.id
                    )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(photo1.number, res.data[0]['number'])
        self.assertNotEqual(photo2.number, res.data[0]['number'])
