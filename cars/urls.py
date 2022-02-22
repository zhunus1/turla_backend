from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    BrandViewSet,
    ClassViewSet,
    TransmissonViewSet,
)

router = DefaultRouter()
router.register(r'brand', BrandViewSet, basename='brans')
router.register(r'class', ClassViewSet, basename='class')
router.register(r'transmission', TransmissonViewSet, basename='transmission')

urlpatterns = [] + router.urls
