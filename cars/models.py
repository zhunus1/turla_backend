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
