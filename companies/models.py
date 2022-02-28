from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.


class DriverRequirement(models.Model):
    
    description = models.TextField(
        verbose_name = "Description",
    )

    min_driver_age = models.PositiveSmallIntegerField(
        verbose_name = "Min driver age",
    )

    min_years_of_license = models.PositiveSmallIntegerField(
        verbose_name = "Min years of license",
    )

    min_young_driver_age  = models.PositiveSmallIntegerField(
        verbose_name = "Min young driver age",
    )

    min_years_of_youth_drivers_license = models.PositiveSmallIntegerField(
        verbose_name = "Min years of youth drivers license",
    )

    created = models.DateTimeField(
        verbose_name = "Created",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Updated",
        auto_now = True,
    )

    class Meta:

        verbose_name = "Driver requirement"
        verbose_name_plural = "Driver requirements"
        ordering = ('-created',)
        

class DriverCondition(models.Model):

    description = models.TextField(
        verbose_name = "Description",
    )

    deposit_fee = MoneyField(
        verbose_name = "Deposit fee",
        max_digits = 8,
        default=0,
    )

    kilometer_limit = models.PositiveIntegerField(
        verbose_name = "Kilometer limit",
    )

    valet_fee = MoneyField(
        verbose_name = "Valet fee",
        max_digits = 8,
        default=0,
    )

    created = models.DateTimeField(
        verbose_name = "Created",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Updated",
        auto_now = True,
    )

    class Meta:

        verbose_name = "Driver condition"
        verbose_name_plural = "Driver conditions"
        ordering = ('-created',)
        
class Company(models.Model):
    name = models.CharField(
        max_length=63,
        verbose_name = "Title",
    )

    rental_conditions = models.TextField(
        verbose_name = "Rental conditions",
    )

    discount_percentage = models.PositiveSmallIntegerField(
        verbose_name = "Discount percentage",
    )

    address = models.CharField(
        max_length=127,
        verbose_name = "Address",
    )

    driver_requirements = models.OneToOneField(
        to = DriverRequirement, 
        on_delete = models.CASCADE,
        related_name = 'company',
        verbose_name = "Driver requirements",
    )

    driver_conditions = models.OneToOneField(
        to = DriverCondition, 
        on_delete = models.CASCADE,
        related_name = 'company',
        verbose_name = "Driver conditions",
    )

    created = models.DateTimeField(
        verbose_name = "Created",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Updated",
        auto_now = True,
    )

    class Meta:

        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ('-created',)
        
    def __str__(self):
        return self.name