# Generated by Django 3.1.13 on 2021-09-24 16:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210924_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginhistory',
            name='latitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)], verbose_name='Location Latitude'),
        ),
        migrations.AlterField(
            model_name='loginhistory',
            name='longitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)], verbose_name='Location Longitude'),
        ),
    ]
