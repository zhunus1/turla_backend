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

class BrandListSearializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'title',
        )


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

class CarListSearializer(serializers.ModelSerializer):
    car_images = CarImageSearializer(many=True)
    car_brand = BrandListSearializer()
    class Meta:
        model = Car
        fields = (
            'id',
            'car_images',
            'car_brand',
            'car_main_image',
            'model_name',
            'model_year',
        )

        #price per day
        #total calculate by selected days
        #deposit

# class CarDetailSearializer(serializers.ModelSerializer):
#     car_images = CarImageSearializer(many=True)
#     car_brand = BrandListSearializer()
#     class Meta:
#         model = Car
#         fields = (
#             'id',
#             'car_brand',
#             'model_name',
#             'model_year',
#             'car_main_image',
#             'car_images',
#         )
#         #rating score 

#         #car class
#         #transmission
#         #fuel type
#         #seats
#         #body type