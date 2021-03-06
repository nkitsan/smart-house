# Generated by Django 2.0.13 on 2019-04-27 20:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarbonDioxide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CarbonDioxideSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controller_ip', models.GenericIPAddressField()),
                ('controller_gpio', models.PositiveSmallIntegerField()),
                ('control_mode', models.BooleanField(default=True)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Humidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HumiditySensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controller_ip', models.GenericIPAddressField()),
                ('controller_gpio', models.PositiveSmallIntegerField()),
                ('preffered_value', models.FloatField(default=30.0, validators=[django.core.validators.MinValueValidator(30.0), django.core.validators.MaxValueValidator(60.0)])),
                ('control_mode', models.BooleanField(default=True)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controller_ip', models.GenericIPAddressField()),
                ('controller_gpio', models.PositiveSmallIntegerField()),
                ('preffered_value', models.FloatField(default=22.0, validators=[django.core.validators.MinValueValidator(20.0), django.core.validators.MaxValueValidator(25.0)])),
                ('control_mode', models.BooleanField(default=True)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
    ]
