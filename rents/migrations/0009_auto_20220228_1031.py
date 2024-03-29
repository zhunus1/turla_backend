# Generated by Django 3.2.12 on 2022-02-28 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('rents', '0008_auto_20220228_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='driver_conditions',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='companies.drivercondition', verbose_name='Driver conditions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='driver_requirements',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='companies.driverrequirement', verbose_name='Driver requirements'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rent',
            name='features',
            field=models.ManyToManyField(related_name='rents_features', to='rents.RentFeature', verbose_name='Feature'),
        ),
    ]
