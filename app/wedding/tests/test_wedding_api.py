from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Wedding

from wedding.serializers import WeddingSerializer

WEDDINGS_URL = reverse('wedding:wedding-list')
CREATE_WEDDING_URL = reverse('wedding:create')


class WeddingTests(TestCase):
    """Test module for POST wedding API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_wedding_success(self):
        """Test creating wedding with valid credentials is successful"""
        wedding_data = {
            'name': 'Simpsons',
            'email': 'test@email.com',
            'date': '06/01/2021'
        }

        res = self.client.post(CREATE_WEDDING_URL, wedding_data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_retrieve_wedding_list(self):

        Wedding.objects.create(
            name='Simpsons',
            email='test@email.com',
            date='06/01/2021'
        )

        Wedding.objects.create(
            name='Smith',
            email='test2@email.com',
            date='08/01/2021'
        )
        response = self.client.get(WEDDINGS_URL)
        weddings = Wedding.objects.all()
        serializer = WeddingSerializer(weddings, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_wedding_instance(self):

        wedding_data1 = {
            'name': 'Simpsons',
            'email': 'test@email.com',
            'date': '06/01/2021'
        }

        wedding_data2 = {
            'name': 'Griffins',
            'email': 'test@email.com',
            'date': '11/22/2022'
        }

        res = self.client.post(CREATE_WEDDING_URL, wedding_data1)
        res2 = self.client.post(CREATE_WEDDING_URL, wedding_data2)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res2.status_code, status.HTTP_201_CREATED)

        weddings = Wedding.objects.all()
        response = self.client.get(
                "/api/v1/weddings/remove/?wedding=% s" % weddings[0].id
                                )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response2 = self.client.get(WEDDINGS_URL)
        serializer = WeddingSerializer(weddings, many=True)
        self.assertEqual(response2.data, serializer.data)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertIn(weddings[0].name, response2.data[0]['name'])
