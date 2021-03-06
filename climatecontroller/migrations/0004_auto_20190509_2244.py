# Generated by Django 2.0.13 on 2019-05-09 19:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatecontroller', '0003_auto_20190509_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbondioxidecontroller',
            name='max_value',
            field=models.FloatField(default=1400.0, validators=[django.core.validators.MinValueValidator(1400.0), django.core.validators.MaxValueValidator(2000.0)]),
        ),
        migrations.AlterField(
            model_name='carbondioxidecontroller',
            name='min_value',
            field=models.FloatField(default=800.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1350.0)]),
        ),
    ]
