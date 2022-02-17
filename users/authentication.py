import json
import logging
from django.conf import settings
from django.utils import timezone
from rest_framework import exceptions, status
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.core.exceptions import ObjectDoesNotExist
from .exceptions import (
    TokenExpired,
    UserNotFound,
)
from .utils import (
    get_user_from_token,
)

logger = logging.getLogger(__name__)


class TurlaUserAuthentication(BaseAuthentication):
    TOKEN_PREFIX = 'TurlaUser'
    def authenticate(self, request):
        try:
            prefix, token = get_authorization_header(request).decode().split(" ", 1)
            if not token:
                return None
            if prefix != TurlaUserAuthentication.TOKEN_PREFIX:
                return None
            return get_user_from_token(token), token
        except Exception as e:
            print(e)
            return None
