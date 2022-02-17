import logging
import requests
import json
from django.conf import settings
from rest_framework import status
from django.utils import timezone
from django.shortcuts import render
from django.utils.translation import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated
from .models import (
    TurlaUser,
    TurlaUserToken,
)
from .authentication import (
    TurlaUserAuthentication,
)
from .serializers import (
    PhoneNumberSerializer,
    TurlaUserSerializer,
    TokenSerializer,
)
from .utils import (
    create_time_stamp,
    create_token_for_user,
    encrypt,
    decrypt,
)

logger = logging.getLogger(__name__)

# Create your views here.

class SignUpView(APIView):
    def post(self, request):
        serializer = TurlaUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Reads temporary token and returns constant token
class SignInView(APIView):

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tempToken = serializer.validated_data['token']

        payload = bytes.fromhex(decrypt(tempToken))
        data = json.loads(payload)

        phone_number = data[0]
        created = datetime.strptime(data[1], '%Y-%m-%d %H:%M:%S')

        if created + timedelta(seconds=settings.FIREBASE_TOKEN_TIME_EXPIRATION) <= timezone.now():
            return Response(data={'message': ugettext('Token expired')}, status=status.HTTP_403_FORBIDDEN)

        try:
            app_user = TurlaUser.objects.get(phone_number=phone_number)
            user_agent = request.headers['User-Agent']
            token = create_token_for_user(app_user, user_agent)
            serializer.validated_data['token'] = token
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except TurlaUser.DoesNotExist:
            return Response(data={'message': ugettext('Invalid token')}, status=status.HTTP_403_FORBIDDEN)


#Sends temporary token to Firebase
class HandShakeView(APIView):

    def post(self, request):
        serializer = PhoneNumberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']

        time_stamp = create_time_stamp(phone_number)
        payload = json.dumps(time_stamp)
        tempToken = encrypt(payload.encode().hex())

        data = {
            'phone_number': phone_number.as_e164,
            'tempToken': tempToken,
        }

        if TurlaUser.objects.filter(phone_number=phone_number.as_e164).exists():
            url = '/firebase/tokens/'
        else:
            url = '/firebase/users/'

        response = requests.post(
            settings.FIREBASE_API_URL + url,
            headers={
                'x-api-key': settings.FIREBASE_API_KEY,
            },
            data=data,
            timeout=30,
        )
        print(response)
        return Response(serializer.data, status=status.HTTP_200_OK)
