from django.urls import path, include
from rest_framework.routers import DefaultRouter

from wedding import views

router = DefaultRouter()
router.register('weddings', views.WeddingViewSet)
router.register('guests', views.GuestViewSet)

app_name = 'wedding'

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.CreateWeddingView.as_view(), name='create'),
    path(
            'create_guest/',
            views.CreateGuestView.as_view(),
            name='create_guest'
        ),
    path(
            'create_photo/',
            views.CreatePhotoView.as_view(),
            name='create_photo'
        ),
]
