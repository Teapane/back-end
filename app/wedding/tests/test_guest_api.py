from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Wedding
from core.models import Guest

from wedding.serializers import GuestSerializer


CREATE_WEDDING_URL = reverse('wedding:create')
GUESTS_URL = reverse('wedding:guest-list')
CREATE_GUEST_URL = reverse('wedding:create_guest')


class PostGuestTests(TestCase):
    """Test module for POST guest API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_guest_success(self):
        "Test creating guest with valid credentials is successful"""

        wedding = Wedding(
                        name='Simpsons',
                        email='simpsonwed@gmail.com',
                        date='2345675432'
                        )
        wedding.save()

        guest_data = {
            'name': 'Uncle Johnny',
            'phone_number': '3450983458',
            'wedding': wedding.id
        }

        res = self.client.post(CREATE_GUEST_URL, guest_data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)


class GetAllGuestsTests(TestCase):
    """Test module for GET all guests API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_guest_list(self):
        wedding1 = Wedding.objects.create(
            name='Bart',
            email='test@email.com',
            date='October 10th, 2022'
        )

        wedding2 = Wedding.objects.create(
            name='Bart',
            email='test@email.com',
            date='October 10th, 2022'
        )

        guest1 = Guest.objects.create(
            name='Uncle Johnny',
            phone_number='3450983458',
            wedding=wedding1
        )

        guest2 = Guest.objects.create(
            name='Aunt Joan',
            phone_number='3450962384',
            wedding=wedding1
        )

        guest3 = Guest.objects.create(
            name='Grandma Charlotte',
            phone_number='34523462384',
            wedding=wedding2
        )

        response = self.client.get(
                        "/api/v1/weddings/guests/?wedding=% s" % wedding1.id
                                )
        guests = guest1.all_guests_given_wedding_id(wedding1.id)
        serializer = GuestSerializer(guests, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertIn(guest2.name, response.data[0]['name'])
        self.assertIn(guest1.name, response.data[1]['name'])
        self.assertNotIn(guest3.name, response.data[0]['name'])
        self.assertNotIn(guest3.name, response.data[1]['name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
