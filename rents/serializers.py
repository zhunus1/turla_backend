from rest_framework import serializers
from .models import (
    Rent,
)
from cars.serializers import (
    CarListSearializer,
)

class RentListSearializer(serializers.ModelSerializer):
    car = CarListSearializer()
    class Meta:
        model = Rent
        fields = (
            'id',
            'car',
            'rent_payment',
            'total_cost',
            'deposit',
        )