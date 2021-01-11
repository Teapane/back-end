from django.urls import path, include
from rest_framework.routers import DefaultRouter

from wedding import views

router = DefaultRouter()
router.register('weddings', views.WeddingViewSet)
router.register(r'guests', views.GuestViewSet, basename='guest')

app_name = 'wedding'

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.CreateWeddingView.as_view(), name='create'),
    path(
            'guest/create/',
            views.CreateGuestView.as_view(),
            name='create_guest'
        ),
    path(
            'photo/create/',
            views.CreatePhotoView.as_view(),
            name='create_photo'
        ),
]
