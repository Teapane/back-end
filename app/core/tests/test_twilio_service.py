from django.test import TestCase

from django.http import HttpResponse
from twilio.rest import Client

from core.models import Wedding
from core.models import Guest
from core.models import Photo


class NotificationSms(TestCase):

    def test_notification_success(self):
        """Test sending notification is successful"""
        expected = HttpResponse("messages sent!", 200)
        self.assertEqual(twilio_service.notification_sms(), expected)
