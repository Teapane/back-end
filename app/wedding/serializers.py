from rest_framework import serializers
from core.models import Wedding
from core.models import Guest
from core.models import Photo


class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = ('id', 'name', 'email', 'date', 'image')


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'name', 'phoneNumber', 'wedding')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'number', 'description', 'guest', 'weddingId')
