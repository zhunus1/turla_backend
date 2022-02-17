from django.utils.translation import *
from rest_framework.exceptions import (
    APIException,
    NotFound,
    PermissionDenied,
    NotAuthenticated,
)


class TokenExpired(NotAuthenticated):
    status_code = 403
    default_detail = ugettext("Access token expired")
    default_code = "forbidden"


class UserNotFound(NotAuthenticated):
    status_code = 403
    default_detail = ugettext("User not found")
    default_code = "forbidden"
