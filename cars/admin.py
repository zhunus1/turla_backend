from django.contrib import admin
from .models import (
    Brand,
    Class,
    Transmisson,
)
# Register your models here.
admin.site.register(Brand)
admin.site.register(Class)
admin.site.register(Transmisson)