from rest_framework import serializers
from .models import (
    Brand,
    Class,
    Transmisson,
    Car,
    CarImage
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


class CarImageSearializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = CarImage
        fields = (
            'id',
            'image_url',
        )

    def get_image_url(self, car_image):
        request = self.context.get('request')
        image_url = car_image.image.url
        return request.build_absolute_uri(image_url)


class BrandListSearializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'title',
        )

class ClassListSearializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = (
            'id',
            'title',
        )

class TransmissonListSearializer(serializers.ModelSerializer):
    class Meta:
        model = Transmisson
        fields = (
            'id',
            'title',
        )

class CarListSearializer(serializers.ModelSerializer):
    car_brand = BrandListSearializer()
    class Meta:
        model = Car
        fields = (
            'id',
            'car_main_image',
            'car_brand',
            'model_name',
            'model_year',
        )

class CarDetailSearializer(serializers.ModelSerializer):
    car_brand = BrandListSearializer()
    car_class = ClassListSearializer()
    car_transmission = TransmissonListSearializer()

    class Meta:
        model = Car
        fields = (
            'id',
            'car_brand',
            'model_name',
            'model_year',
            'car_main_image',
            'car_class',
            'car_transmission',
            'fuel_type',
            'seat_number',
            'car_type',
        )