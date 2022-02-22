from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Rent,
)
from .serializers import (
    RentListSearializer,
    RentFilterSerializer
)
from .filters import (
    RentFilter,
)

# Create your views here.

class RentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RentListSearializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = RentFilter

    #Add filter and show all rents with correspondin start and end
    def get_queryset(self):
        queryset = Rent.objects \
            .select_related(
                'car',
            ) \
            .prefetch_related(
                'drop_off',
            ) \
            .all()
        return queryset

    def filter_queryset(self, queryset):
        serialzier = RentFilterSerializer(data=self.request.query_params)
        serialzier.is_valid(raise_exception=True)

        start_date = serialzier.validated_data.get('start_date')
        end_date = serialzier.validated_data.get('end_date')

        queryset = queryset.exclude(
            Q(start_date__lte=end_date),
            Q(end_date__gte=start_date),
        )
        #exclude
        return super().filter_queryset(queryset)
