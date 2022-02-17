from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class TurlaUser(AbstractBaseUser):

    password = None

    first_name = models.CharField(
        verbose_name = "First name",
        max_length = 127,
    )

    last_name = models.CharField(
        verbose_name = "Last name",
        max_length = 127,
    )

    phone_number = PhoneNumberField(
        verbose_name = "Phone number",
    )

    is_customer = models.BooleanField(
        verbose_name = "Is customer",
        default = False,
    )

    created = models.DateTimeField(
        verbose_name = "Created",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Updated",
        auto_now = True,
    )

    USERNAME_FIELD = 'phone_number'

    class Meta:

        verbose_name = "TurlaUser"
        verbose_name_plural = "TurlaUsers"
        ordering = ('-created',)

    def __str__(self):
        return '%s' % self.phone_number


class TurlaUserToken(models.Model):

    turla_user = models.ForeignKey(
        verbose_name = "Turla User",
        to = TurlaUser,
        related_name = 'tokens',
        on_delete = models.CASCADE,
    )

    user_agent = models.CharField(
        verbose_name = "User agent",
        max_length = 1023,
    )

    token = models.CharField(
        verbose_name = "Token",
        max_length = 255,
        unique = True,
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

        verbose_name = "Turla user token"
        verbose_name_plural = "Turla user tokens"
        ordering = ('-created',)

    def __str__(self):
        return '%s' % self.appuser.phone_number