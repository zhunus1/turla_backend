from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    BrandSearializer,
    ClassSearializer,
    TransmissonSearializer,
    BrandListSearializer
)
from .models import (
    Brand,
    Class,
    Transmisson,
)

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandListSearializer

class ClassViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSearializer

class TransmissonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transmisson.objects.all()
    serializer_class = TransmissonSearializer