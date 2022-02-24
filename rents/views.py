import calendar
import json
from calendar import monthrange
import datetime
import itertools
from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import (
    Rent,
)
from .serializers import (
    RentListSearializer,
    RentFilterSerializer,
    RentByLocationSerializer,
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
        serializer = RentFilterSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)

        start_date = serializer.validated_data.get('start_date')
        end_date = serializer.validated_data.get('end_date')

        queryset = queryset.exclude(
            Q(start_date__lte=end_date),
            Q(end_date__gte=start_date),
        )
        return super().filter_queryset(queryset)
    
    def count_free(self, months, rent):
        #Today is a limit, you can not rent a car in the past
        current_day_year = datetime.date.today()
        last_day_year = datetime.date.today().replace(month=12, day=31)

        current_year = datetime.date.today().year
        start_date = rent.start_date
        end_date = rent.end_date

        if (start_date == None and end_date == None):
            for i in range(1, 13):
                for j in range(1, monthrange(current_year, list(months)[i-1])[1]+1):
                    months[i][j] += 1
        elif (start_date.month == end_date.month):
            for i in range(1, start_date.day):
                months[start_date.month][i] += 1
            for j in range(end_date.day + 1, monthrange(start_date.year, start_date.month)[1] + 1):
                months[start_date.month][j] += 1
        else:
            for i in range(1, start_date.day):
                months[start_date.month][i] += 1
            for j in range(end_date.day + 1, monthrange(end_date.year, end_date.month)[1]):
                months[end_date.month][j] += 1


    @action(detail=False, methods=['GET'])
    def information(self, request):
        queryset = self.get_queryset()

        serializer = RentByLocationSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        
        pick_up = serializer.validated_data.get('pick_up')
        drop_off = serializer.validated_data.get('drop_off')
        
        queryset = queryset \
            .filter(pick_up=pick_up,
                    drop_off=drop_off)

        year = datetime.date.today().year
        
        months = dict.fromkeys(range(1, 13))
        for i in range(1, 13):
            days = list(itertools.chain.from_iterable(calendar.monthcalendar(year, i)))
            clean_days = dict.fromkeys([day for day in days if day != 0], 0)
            months[i] = clean_days
        

        for i in range(len(queryset)):
            self.count_free(months, queryset[i])

        data = json.dumps(months)

        return Response(data)

