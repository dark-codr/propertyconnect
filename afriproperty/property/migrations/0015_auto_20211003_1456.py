# Generated by Django 3.1.13 on 2021-10-03 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20210930_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertycompare',
            old_name='p_one',
            new_name='property',
        ),
        migrations.RemoveField(
            model_name='propertycompare',
            name='p_three',
        ),
        migrations.RemoveField(
            model_name='propertycompare',
            name='p_two',
        ),
        migrations.RemoveField(
            model_name='propertycompare',
            name='slug',
        ),
    ]
