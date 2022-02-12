from django.db import models

# Create your models here.
class Country(models.Model):

    title = models.CharField(
        max_length=255,
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

        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ('-created',)
        
    def __str__(self):
        return self.title

class City(models.Model):

    country = models.ForeignKey(
        to = Country, 
        on_delete = models.CASCADE,
        related_name='cities',
        verbose_name = "Country",
    )

    title = models.CharField(
        max_length = 255,
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

        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ('-created',)
        
    def __str__(self):
        return self.title


class Location(models.Model):

    city = models.ForeignKey(
        to = City, 
        on_delete = models.CASCADE,
        related_name = 'locations',
        verbose_name = "City",
    )

    title = models.CharField(
        max_length = 255,
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

        verbose_name = "Location"
        verbose_name_plural = "Locations"
        ordering = ('-created',)
        
    def __str__(self):
        return self.title