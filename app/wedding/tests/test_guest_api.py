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


class GuestTests(TestCase):
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
            'phoneNumber': '3450983458',
            'wedding': wedding.id
        }

        res = self.client.post(CREATE_GUEST_URL, guest_data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

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
            phoneNumber='3450983458',
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

    def test_delete_guest_instance(self):

        wedding1 = Wedding(
                        name='Simpsons',
                        email='simpsonwed@gmail.com',
                        date='2345675432'
                        )
        wedding1.save()

        wedding2 = Wedding(
                        name='Griffins',
                        email='griffinwed@gmail.com',
                        date='2345675432'
                        )
        wedding2.save()

        guest_data1 = {
            'name': 'Uncle Johnny',
            'phoneNumber': '3450983458',
            'wedding': wedding1.id
        }

        guest_data2 = {
            'name': 'Lois',
            'phoneNumber': '3450983458',
            'wedding': wedding1.id
        }

        guest_data3 = {
            'name': 'Chris',
            'phoneNumber': '3450983458',
            'wedding': wedding2.id
        }

        res = self.client.post(CREATE_GUEST_URL, guest_data1)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        res2 = self.client.post(CREATE_GUEST_URL, guest_data2)
        self.assertEqual(res2.status_code, status.HTTP_201_CREATED)
        res3 = self.client.post(CREATE_GUEST_URL, guest_data3)
        self.assertEqual(res3.status_code, status.HTTP_201_CREATED)

        guests = Guest.objects.all()
        response = self.client.get(
                "/api/v1/weddings/remove_guest/?guest=% s" % guests[0].id
                                )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response2 = self.client.get(
                        "/api/v1/weddings/guests/?wedding=% s" % wedding1.id
                                )
        guests2 = guests[0].all_guests_given_wedding_id(wedding1.id)
        serializer = GuestSerializer(guests2, many=True)
        self.assertEqual(response2.data[0]['name'], serializer.data[0]['name'])
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
