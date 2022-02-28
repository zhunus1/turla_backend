from rest_framework import serializers
from .models import (
    Rent,
    RentFeature
)
from cars.serializers import (
    CarListSearializer,
    CarDetailSearializer,
)
from companies.serializers import (
    CompanyDetailSearializer,
)

class RentFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentFeature
        fields = (
            'id',
            'title',
        )

class RentListSearializer(serializers.ModelSerializer):
    car = CarListSearializer()
    class Meta:
        model = Rent
        fields = (
            'id',
            'car',
            'price',
            'total_cost',
            'deposit',
        )

class RentDetailSearializer(serializers.ModelSerializer):
    car = CarDetailSearializer()
    features = RentFeatureSerializer(many=True)
    company = CompanyDetailSearializer()
    class Meta:
        model = Rent
        fields = (
            'id',
            'car',
            'features',
            'price',
            'deposit',
            'total_cost',
            'total_cost_discount',
            'company',
        )


class RentFilterSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required = False)
    end_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required = False)

class RentByLocationSerializer(serializers.Serializer):
    pick_up = serializers.IntegerField()
    drop_off = serializers.IntegerField()