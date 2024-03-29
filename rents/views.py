import calendar
import json
from calendar import monthrange
import datetime
from datetime import timedelta
import itertools
from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import (
    Rent,
)
from .serializers import (
    RentListSearializer,
    RentDetailSearializer,
    RentFilterSerializer,
    RentByLocationSerializer,
)
from .filters import (
    RentFilter,
)

# Create your views here.

class RentViewSet(viewsets.ReadOnlyModelViewSet):
    #filter by age between 25 - 70 driver requirements minimum driver age

    filter_backends = (DjangoFilterBackend,)
    filter_class = RentFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return RentListSearializer
        return RentDetailSearializer

        

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

        if start_date and end_date:

            queryset = queryset.exclude(
                Q(start_date__lte=end_date),
                Q(end_date__gte=start_date),
            )
        return super().filter_queryset(queryset)
    
    def count_free(self, months, rent):

        current_day_year = datetime.date.today()
        last_day_year = datetime.date.today().replace(month=12, day=31)

        current_year = datetime.date.today().year
        start_date = rent.start_date
        end_date = rent.end_date


        if start_date == None and end_date == None:
            for i in range(1, 13):
                for j in range(1, monthrange(current_year, list(months)[i-1])[1]+1):
                    months[i][j] += 1
        else:
            start = None
            end = None
            for j in range(current_day_year.month, start_date.month + 1):
                if j == start_date.month:
                    start = current_day_year.day
                    end = start_date.day

                    for i in range(start, end):
                        months[j][i] += 1
                else:
                    start = current_day_year.day
                    if current_day_year.month == j:
                        end = start_date.day
                    else:
                        end = monthrange(current_year, j)[1]

                    for i in range(start, monthrange(current_year, j)[1] + 1):
                        months[j][i] += 1
                    for k in range(1, end + 1):
                        months[j + 1][k] += 1
            # теперь от даты конца и до конца года
            for j in range(start_date.month, 13):
                if j == start_date.month:
                    start = end_date.day
                    end = monthrange(current_year, j)[1] + 1
                    for i in range(start, end):
                        months[j][i] += 1
                else:
                    start = 1
                    end = monthrange(current_year, j)[1] + 1
                    for i in range(start, end):
                        months[j][i] += 1



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
        
        return Response(data, status=status.HTTP_200_OK)

