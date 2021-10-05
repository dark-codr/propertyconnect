# Generated by Django 3.1.13 on 2021-10-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_agentprofile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='googleplus',
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, help_text='https://www.google.com/profilename/', null=True, unique=True, verbose_name='Instagram Profile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('Individual [Searching for property]', 'Individual [Searching for property]'), ('Property Owner', 'Property Owner'), ('Estate Agent', 'Estate Agent'), ('Property Developers/Management Company', 'Property Developer')], default='Individual [Searching for property]', max_length=50, null=True, verbose_name='Account Type'),
        ),
    ]
