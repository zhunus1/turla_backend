from rest_framework import serializers
from .models import (
    Country,
    City,
    Location
)

class CountrySearializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id',
            'title',
        )

class CitySearializer(serializers.ModelSerializer):
    country = CountrySearializer()
    class Meta:
        model = City
        fields = (
            'id',
            'title',
            'country',
        )

class LocationSearializer(serializers.ModelSerializer):
    city = CitySearializer()
    class Meta:
        model = Location
        fields = (
            'id',
            'title',
            'city',
        )