# Generated by Django 3.2.12 on 2022-02-15 06:03

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TurlaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=127, verbose_name='First name')),
                ('last_name', models.CharField(max_length=127, verbose_name='Last name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number')),
                ('is_customer', models.BooleanField(default=False, verbose_name='Is customer')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'TurlaUser',
                'verbose_name_plural': 'TurlaUsers',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='TurlaUserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=1023, verbose_name='User agent')),
                ('token', models.CharField(max_length=255, unique=True, verbose_name='Token')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('turla_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to='users.turlauser', verbose_name='Turla User')),
            ],
            options={
                'verbose_name': 'Turla user token',
                'verbose_name_plural': 'Turla user tokens',
                'ordering': ('-created',),
            },
        ),
    ]
