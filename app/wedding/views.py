# import json
# from django.http import JsonResponse
# from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser

from core.models import Wedding
from core.models import Guest
from core.models import Photo

from wedding import serializers
from wedding.serializers import WeddingSerializer
from wedding.serializers import GuestSerializer
from wedding.serializers import PhotoSerializer


class WeddingViewSet(viewsets.ModelViewSet):
    """Manage weddings in the database"""
    queryset = Wedding.objects.all()
    serializer_class = serializers.WeddingSerializer


class CreateWeddingView(generics.CreateAPIView):
    """Create a new wedding in the system"""
    serializer_class = WeddingSerializer


class GuestViewSet(viewsets.ModelViewSet):
    """Manage guests in the database"""
    serializer_class = serializers.GuestSerializer

    def get_queryset(self):
        queryset = Guest.objects.filter(
                    wedding=self.request.query_params['wedding']
                                        )
        return queryset


class CreateGuestView(generics.CreateAPIView):
    """Create a new guest in the system"""
    serializer_class = GuestSerializer


class CreatePhotoView(generics.CreateAPIView):
    """Create a new photo in the system"""
    serializer_class = PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """Manage photos in the database"""
    serializer_class = serializers.PhotoSerializer

    def get_queryset(self):
        queryset = Photo.objects.filter(
                    weddingId=self.request.query_params['weddingId']
                                        )
        return queryset


class DeleteWeddingView(viewsets.ModelViewSet):
    """Delete a wedding in the system"""
    serializer_class = serializers.WeddingSerializer

    def get_queryset(self):
        queryset = Wedding.objects.filter(
                    id=self.request.query_params['wedding']
                                        )
        wedding = queryset[0]
        wedding.delete()
        return queryset
