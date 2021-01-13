from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client

import code

def notification_sms(request):
    message_notification = ("Have you played the incredible TwilioQuest "
                                                "yet? Grab it here: https://www.twilio.com/quest")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    # notification = client.notify.services('ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    # .notifications.create(
    #     # We recommend using a GUID or other anonymized identifier for Identity
    #     identity='00000001',
    #     body='guest.name you're in photo(s) guest.photos')

    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)
