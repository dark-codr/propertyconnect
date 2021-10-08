# Generated by Django 3.1.13 on 2021-09-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20210928_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_area',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Area Sq/Ft'),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='if your price type is sq/ft, then the price cost should be by a unit of the property area square feet and leave the total we will automatically round it up for you by the total area numbers you have ', max_digits=20, verbose_name='Property Price'),
        ),
    ]