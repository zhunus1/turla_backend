# Generated by Django 3.2.12 on 2022-02-17 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_carimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carimage',
            options={'ordering': ('-created',), 'verbose_name': 'Car image', 'verbose_name_plural': 'Car images'},
        ),
    ]