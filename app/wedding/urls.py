from django.urls import path, include
from rest_framework.routers import DefaultRouter

from wedding import views

router = DefaultRouter()
router.register('weddings', views.WeddingViewSet)

app_name = 'wedding'

urlpatterns = [
    path('', include(router.urls))
]
