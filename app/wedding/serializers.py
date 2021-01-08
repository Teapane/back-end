from rest_framework import serializers
from core.models import Wedding
from core.models import Guest


class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = ('id', 'name', 'email', 'date', 'image')


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'name', 'phone_number', 'wedding')
