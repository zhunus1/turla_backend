from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import (
    TurlaUser,
)



class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()


class TurlaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurlaUser
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'is_customer',
        )
