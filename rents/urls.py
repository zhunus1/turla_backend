from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    RentViewSet,
)

router = DefaultRouter()
router.register(r'rents', RentViewSet, basename='rents')

urlpatterns = [] + router.urls
