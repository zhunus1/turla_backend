from django.contrib import admin
from .models import (
    Company,
    DriverRequirement,
    DriverCondition
)
# Register your models here.
admin.site.register(Company)
admin.site.register(DriverRequirement)
admin.site.register(DriverCondition)