from django.db import models
from djmoney.models.fields import MoneyField
from cars.models import (
    Car,
)
from locations.models import (
    Location,
)
from companies.models import (
    DriverCondition,
    DriverRequirement
)
# Create your models here.

class RentFeature(models.Model):
    title = models.CharField(
        max_length=31,
        verbose_name = "Title",
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

        verbose_name = "Rent feature"
        verbose_name_plural = "Rent features"
        ordering = ('-created',)
        
    def __str__(self):
        return self.title


class Rent(models.Model):
    class DeliveryType(models.TextChoices):
        in_terminal = 'In-terminal Office', ('In-terminal Office')
        office = 'Office', ('Office')
        valet = 'Valet Service', ('Valet Service')
        out_terminal = 'Out of Terminal Valet Service', ('Out of Terminal Valet Service')

    start_date = models.DateTimeField(
        verbose_name = "Start date",
        blank = True,
        null = True
    )

    end_date = models.DateTimeField(
        verbose_name = "End date",
        blank = True,
        null = True
    )
    
    car = models.OneToOneField(
        verbose_name = "Car",
        to = Car,
        related_name = 'rent',
        on_delete = models.CASCADE,
    )

    price = MoneyField(
        verbose_name = "Price",
        max_digits = 6,
        default=0,
    )

    deposit = MoneyField(
        verbose_name = "Deposit",
        max_digits = 8,
        default=0,
    )

    pick_up = models.ManyToManyField(
        verbose_name = "Pick up",
        to = Location,
        related_name = 'rents_pick_up',
    )

    drop_off = models.ManyToManyField(
        verbose_name = "Drop off",
        to = Location,
        related_name = 'rents_drop_off',
    )

    condition = models.TextField(
        verbose_name = "Condition",
    )

    delivery_type = models.CharField(
        max_length=63,
        choices=DeliveryType.choices,
        verbose_name = "Delivery type",
    )

    features = models.ManyToManyField(
        verbose_name = "Feature",
        to = RentFeature,
        related_name = 'rents_features',
    )

    driver_requirements = models.ForeignKey(
        to = DriverRequirement, 
        on_delete = models.CASCADE,
        related_name = 'rents',
        verbose_name = "Driver requirements",
    )

    driver_conditions = models.ForeignKey(
        to = DriverCondition, 
        on_delete = models.CASCADE,
        related_name = 'rents',
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

        verbose_name = "Rent"
        verbose_name_plural = "Rents"
        ordering = ('-created',)
        
    def __str__(self):
        return ('%s - %s') % (str(self.start_date), str(self.end_date))
    
    @property
    def total_cost(self):
        if self.start_date.day == self.end_date.day:
            return self.price.amount
        return self.price.amount * (self.end_date.day - self.start_date.day)