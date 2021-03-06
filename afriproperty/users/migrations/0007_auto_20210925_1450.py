# Generated by Django 3.1.13 on 2021-09-25 13:50

import afriproperty.users.models
from django.db import migrations, models
import django.utils.timezone
import django_resized.forms
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210924_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('cookies_and_tracking', models.BooleanField(default=True, help_text='This is a must have integration to enable us provide you with proper services and security. They do not create any security bridge for you and can only be used to login, signout and even ensure your sessions are still working. You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('google_ads', models.BooleanField(default=True, help_text='These is an advertising and devlivey network service, aimed solely to provide advert placements based on your browser informations. permiting this allows us provide you with adverts directly on our site. Be ensured that this does not constitute any security risk to you. You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('social_account_integration', models.BooleanField(default=True, help_text='Facebook, Instagram, Twitter, Google Plus, Linkedin, these providers are integrated into the website to ensure we have proper informations to provide for our social influence and lead generation. We do not share these information for any other purpose other than statistical analysis. You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('personal_information', models.BooleanField(default=True, help_text='These are personal informations we collect to provide quality and personalised services to you. They include (First Name, Last Name, Phone Number, Social Accounts, Addresses, Photo). You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('commercial_information', models.BooleanField(default=True, help_text='These are informations we collect for commercial purposes and are used for analysis as well as providing accurate data statistics of our services usage. You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('identifiers', models.BooleanField(default=True, help_text='These are informations we collect to prevent fraud, do analysis as well as utilize cloud services. They include Email address, device identifiers (User IDs, IP and Location). You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('internet_or_other_electronic_network_activity_information', models.BooleanField(default=True, help_text='These are informations we collect regarding the user interactions within the website. With this information we can provide cloud services such as Content Delivery Networks for static/asset and media files. You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('age_restricktion', models.BooleanField(default=True, help_text='As a bid to ensure we do not share informations to individuals who are below legal age, we expect a concent to be taken, idemnifying us from any law suit involved with sharing certain or aiding a minor purchase goods and services without a concent from a legal guardian. You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='User IP')),
                ('country', models.CharField(blank=True, max_length=80, null=True, verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Privacy',
                'verbose_name_plural': 'Privacies',
                'ordering': ['-created', '-ip'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='agentprofile',
            name='company_logo',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', help_text='image size: 150x150.', keep_meta=True, null=True, quality=75, size=[150, 150], upload_to=afriproperty.users.models.company_logo),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', help_text='image size: 300x300', keep_meta=True, null=True, quality=75, size=[300, 300], upload_to=afriproperty.users.models.profile_image),
        ),
    ]
