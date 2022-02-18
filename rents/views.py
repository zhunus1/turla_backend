from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Rent,
)
# from .serializers import (
#     RentsByBrendSeriazlier,
# )
# Create your views here.

class RentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rent.objects.all()
    # serializer_class = RentsByBrendSeriazlier

    #Add filter and show all rents with correspondin start and end 