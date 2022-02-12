from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import (
    Country,
    City,
    Location,
)
from .serializers import (
    CitySearializer,
    LocationSearializer
)
# Create your views here.

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSearializer
    filter_backends = (SearchFilter,)
    search_fields = ('city__title', 'title')
