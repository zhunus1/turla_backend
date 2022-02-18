# Generated by Django 3.2.12 on 2022-02-18 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20220218_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='seat_number',
            field=models.CharField(choices=[('2', '2'), ('4', '4'), ('5', '5'), ('7', '7'), ('10', '10')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('SDN', 'Sedan'), ('CPE', 'Coupe'), ('SCR', 'Sports car'), ('WGN', 'Wagon'), ('HTB', 'Hatchback'), ('CNV', 'Convertible'), ('SUV', 'SUV'), ('MNV', 'Minivan'), ('PCK', 'Pickup')], max_length=3),
        ),
    ]