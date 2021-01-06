from rest_framework import viewsets

from core.models import Wedding

from wedding import serializers


class WeddingViewSet(viewsets.ModelViewSet):
    """Manage weddings in the database"""
    queryset = Wedding.objects.all()
    serializer_class = serializers.WeddingSerializer
