from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    LocationViewSet,
)

router = DefaultRouter()
router.register(r'location', LocationViewSet, basename='location')

urlpatterns = [] + router.urls
