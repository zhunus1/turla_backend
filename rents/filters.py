import django_filters as filters
from .models import Rent

class RentFilter(filters.FilterSet):
    brand = filters.CharFilter(field_name='car__car_brand__title')

    class Meta:
        model = Rent
        fields = (
            'brand',
        )