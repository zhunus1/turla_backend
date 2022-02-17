from django.contrib import admin
from .models import (
    Brand,
    Class,
    Transmisson,
    Car,
    CarImage
)
# Register your models here.
admin.site.register(Brand)
admin.site.register(Class)
admin.site.register(Transmisson)
admin.site.register(Car)
admin.site.register(CarImage)