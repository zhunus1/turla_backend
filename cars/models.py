from django.db import models

# Create your models here.
class Brand(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = "Title",
    )
    
    logo = models.ImageField(
        upload_to ='cars/brands/logo/',
        verbose_name = "Logo",
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

        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ('-created',)
        
    def __str__(self):
        return self.title

class Class(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = "Title",
    )
    
    logo = models.ImageField(
        upload_to ='cars/classes/logo/',
        verbose_name = "Logo",
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

        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ('-created',)
        
    def __str__(self):
        return self.title

class Transmisson(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = "Title",
    )
    
    logo = models.ImageField(
        upload_to ='cars/transmissons/logo/',
        verbose_name = "Logo",
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

        verbose_name = "Transmisson"
        verbose_name_plural = "Transmissons"
        ordering = ('-created',)
        
    def __str__(self):
        return self.title


class Car(models.Model):
    class CarEngineCapacity(models.TextChoices):
        LOW_1 = 'L_1', ('< 1000')
        LOW_2 = 'L_2', ('1001 - 1300')
        LOW_3 = 'L_3', ('1301 - 1400')
        LOW_4 = 'L_4', ('1401 - 1600')
        LOW_5 = 'L_5', ('1601 - 1800')
        MEDIUM_1 = 'M_1', ('1801 - 2000')
        MEDIUM_2 = 'M_2', ('2001 - 2500')
        MEDIUM_3 = 'M_3', ('2501 - 3000')
        HIGH_1 = 'H_1', ('3001 - 3500')
        HIGH_2 = 'H_2', ('3501 - 4000')
        HIGH_3 = 'H_3', ('4001 - 10000')
        ELECTRICITY = 'E', ('Electricity')
    
    class CarType(models.TextChoices):
        sedan = 'SDN', ('Sedan')
        coupe = 'CPE', ('Coupe')
        sports_car = 'SCR', ('Sports car')
        wagon = 'WGN', ('Wagon')
        hatchback = 'HTB', ('Hatchback')
        convertible = 'CNV', ('Convertible')
        suv = 'SUV', ('SUV')
        minivan = 'MNV', ('Minivan')
        pickup = 'PCK', ('Pickup')
    
    class SeatNumber(models.TextChoices):
        two = '2', ('2')
        four = '4', ('4')
        five = '5', ('5')
        seven = '7', ('7')
        ten = '10', ('10')
    
    class FuelType(models.TextChoices):
        diesel = 'D', ('Diesel')
        petrol = 'P', ('Petrol')
        electricity = 'E', ('Electricity')
        hybrid = 'H', ('Hybrid')
        gaz = 'G', ('Gaz')
        
    car_brand = models.ForeignKey(
        verbose_name = "Car brand",
        to = Brand,
        related_name = 'cars',
        on_delete = models.CASCADE,
    )

    model_name = models.CharField(
        max_length=255,
        verbose_name = "Model name",
    )

    car_main_image = models.ImageField(
        upload_to ='car/images/main',
        verbose_name = "Car main image",
    )

    model_year = models.CharField(
        max_length=4,
        verbose_name = "Model year",
    )

    car_class = models.ForeignKey(
        verbose_name = "Car class",
        to = Class,
        related_name = 'cars',
        on_delete = models.CASCADE,
    )

    car_transmission = models.ForeignKey(
        verbose_name = "Car transmission",
        to = Transmisson,
        related_name = 'cars',
        on_delete = models.CASCADE,
    )

    engine_capacity = models.CharField(
        max_length=3,
        choices=CarEngineCapacity.choices,
        verbose_name = "Engine capacity",
    )

    car_type = models.CharField(
        max_length=3,
        choices=CarType.choices,
        verbose_name = "Car type",
    )

    seat_number = models.CharField(
        max_length=2,
        choices=SeatNumber.choices,
        verbose_name = "Seat number",
    )

    fuel_type = models.CharField(
        max_length=1,
        choices=FuelType.choices,
        verbose_name = "Fuel type",
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

        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ('-created',)
        
    def __str__(self):
        return "%s %s" % (self.car_brand.title, self.model_name)


class CarImage(models.Model):

    car = models.ForeignKey(
        verbose_name = "Car",
        to = Car,
        related_name = 'car_images',
        on_delete = models.CASCADE,
    )

    image = models.ImageField(
        upload_to ='car/images/others',
        verbose_name = "Image",
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

        verbose_name = "Car image"
        verbose_name_plural = "Car images"
        ordering = ('-created',)
        
    def __str__(self):
        return "%s %s" % (self.car.car_brand.title, model_name)