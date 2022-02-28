# Generated by Django 3.2.12 on 2022-02-28 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0007_auto_20220228_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31, verbose_name='Title')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Rent feature',
                'verbose_name_plural': 'Rent features',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='rent',
            name='features',
            field=models.ManyToManyField(related_name='rents', to='rents.RentFeature', verbose_name='Feature'),
        ),
    ]