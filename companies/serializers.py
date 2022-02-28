from rest_framework import serializers
from .models import (
    DriverCondition,
    DriverRequirement,
    Company
)
class CompanySearializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'rental_conditions',
        )

class DriverConditionSearializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCondition
        fields = (
            'id',
            'description',
            'deposit_fee',
            'kilometer_limit',
            'valet_fee',
        )

class DriverRequirementSearializer(serializers.ModelSerializer):
    class Meta:
        model = DriverRequirement
        fields = (
            'id',
            'description',
            'min_driver_age',
            'min_years_of_license',
            'min_young_driver_age',
            'min_years_of_youth_drivers_license',
        )

class CompanyDetailSearializer(serializers.ModelSerializer):
    driver_requirements = DriverRequirementSearializer()
    driver_conditions = DriverConditionSearializer()
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'rental_conditions',
            'address',
            'driver_conditions',
            'driver_requirements',  
        )