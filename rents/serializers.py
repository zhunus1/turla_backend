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

class RentFilterSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

class RentByLocationSerializer(serializers.Serializer):
    pick_up = serializers.IntegerField()
    drop_off = serializers.IntegerField()