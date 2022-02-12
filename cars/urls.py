from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    BrandViewSet,
    ClassViewSet,
    TransmissonViewSet,
)

router = DefaultRouter()
router.register(r'brand', BrandViewSet)
router.register(r'class', ClassViewSet)
router.register(r'transmission', TransmissonViewSet)

urlpatterns = [] + router.urls
