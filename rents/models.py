from django.db import models
from djmoney.models.fields import MoneyField
from cars.models import (
    Car,
)
from locations.models import (
    Location,
)
# Create your models here.

class Rent(models.Model):
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

    rent_payment = MoneyField(
        verbose_name = "Rent payment",
        max_digits = 6,
    )

    deposit = MoneyField(
        verbose_name = "Deposit",
        max_digits = 8,
    )

    pick_up = models.ManyToManyField(
        verbose_name = "Pick up",
        to = Location,
        related_name = 'rents_pick_up',
    )

    drop_off = models.ManyToManyField(
        verbose_name = "Drop off",
        to = Location,
        default = pick_up,
        related_name = 'rents_drop_off',
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
            return self.rent_payment.amount
        return self.rent_payment.amount * (self.end_date.day - self.start_date.day)