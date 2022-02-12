from rest_framework import serializers
from .models import (
    Brand,
    Class,
    Transmisson
)

class BrandSearializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    class Meta:
        model = Brand
        fields = (
            'id',
            'title',
            'logo_url',
        )

    def get_logo_url(self, brand):
        request = self.context.get('request')
        logo_url = brand.logo.url
        return request.build_absolute_uri(logo_url)

class ClassSearializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    class Meta:
        model = Class
        fields = (
            'id',
            'title',
            'logo_url',
        )

    def get_logo_url(self, car_class):
        request = self.context.get('request')
        logo_url = car_class.logo.url
        return request.build_absolute_uri(logo_url)

class TransmissonSearializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    class Meta:
        model = Transmisson
        fields = (
            'id',
            'title',
            'logo_url',
        )

    def get_logo_url(self, transmisson):
        request = self.context.get('request')
        logo_url = transmisson.logo.url
        return request.build_absolute_uri(logo_url)