# Generated by Django 3.1.13 on 2021-09-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20210926_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
