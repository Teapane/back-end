from rest_framework import viewsets
from rest_framework import generics

from core.models import Wedding
from core.models import Guest

from wedding import serializers
from wedding.serializers import WeddingSerializer
from wedding.serializers import GuestSerializer


class WeddingViewSet(viewsets.ModelViewSet):
    """Manage weddings in the database"""
    queryset = Wedding.objects.all()
    serializer_class = serializers.WeddingSerializer


class CreateWeddingView(generics.CreateAPIView):
    """Create a new wedding in the system"""
    serializer_class = WeddingSerializer


class GuestViewSet(viewsets.ModelViewSet):
    """Manage guests in the database"""
    queryset = Guest.objects.all()
    serializer_class = serializers.GuestSerializer


class CreateGuestView(generics.CreateAPIView):
    """Create a new guest in the system"""
    serializer_class = GuestSerializer
