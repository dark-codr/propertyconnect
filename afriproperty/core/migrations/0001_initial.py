# Generated by Django 3.1.13 on 2021-09-25 13:50

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSubscribe',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Please')),
                ('subscribed', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Email Subscriber',
                'verbose_name_plural': 'Email Subscribers',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
    ]
