from rest_framework import serializers
from .models import (
    Rent,
)

class RentListSearializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = (
            'id',
            'rent_payment',
            'total_cost',
            'deposit',
        )
