from rest_framework import serializers
from core.models import Wedding


class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = ('id', 'name', 'email', 'date', 'image')
