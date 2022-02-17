from django.contrib import admin
from .models import (
    TurlaUser,
    TurlaUserToken,
)

# Register your models here.
admin.site.register(TurlaUser)
admin.site.register(TurlaUserToken)