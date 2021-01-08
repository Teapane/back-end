from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Wedding

from wedding.serializers import WeddingSerializer

WEDDINGS_URL = reverse('wedding:wedding-list')
CREATE_WEDDING_URL = reverse('wedding:create')


class PostWeddingTests(TestCase):
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


class GetAllWeddingsTests(TestCase):
    """Test module for GET all weddings API"""

    def setUp(self):
        self.client = APIClient()

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

    def test_retrieve_wedding_list(self):
        response = self.client.get(WEDDINGS_URL)
        weddings = Wedding.objects.all()
        serializer = WeddingSerializer(weddings, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
