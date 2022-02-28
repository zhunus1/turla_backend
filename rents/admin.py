from django.contrib import admin
from .models import (
    Rent,
    RentFeature
)
# Register your models here.
admin.site.register(Rent)
admin.site.register(RentFeature)