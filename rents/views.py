from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Rent,
)
from .serializers import (
    RentListSearializer,
)
# Create your views here.

class RentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentListSearializer
