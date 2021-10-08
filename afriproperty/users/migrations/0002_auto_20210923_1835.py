# Generated by Django 3.1.13 on 2021-09-23 17:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(blank=True, max_length=500, null=True, unique=True, verbose_name='Bank Name')),
                ('country', models.CharField(blank=True, max_length=500, null=True, verbose_name='Bank Country')),
                ('currency', models.CharField(blank=True, max_length=3, null=True, verbose_name='Bank currency')),
                ('slug', models.SlugField(blank=True, max_length=700, null=True, unique=True)),
                ('bank_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='Bank Code')),
                ('bank_id', models.CharField(blank=True, max_length=5, null=True, verbose_name='Bank ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True, 'ordering': ['first_name', 'last_name'], 'verbose_name': 'User Account', 'verbose_name_plural': 'User Accounts'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='Account_type',
            field=models.CharField(choices=[('Individual [Searching for property]', 'Individual [Searching for property]'), ('Property Owner', 'Property Owner'), ('Estate Agent', 'Estate Agent'), ('Property Developer', 'Property Developer')], default='Individual [Searching for property]', max_length=50, null=True, verbose_name='Account Type'),
        ),
        migrations.AddField(
            model_name='user',
            name='accept_terms',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='has_testified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='user',
            name='postcode',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Postcode (Optional)'),
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('property_request', models.BooleanField(default=True, help_text='Recieve Notifications when someone makes request for a property?')),
                ('direct_message', models.BooleanField(default=True, help_text='Recieve Notifications from direct messages?')),
                ('email_notification', models.BooleanField(default=True, help_text='Recieve Notifications via verified email address?')),
                ('send_newsletter', models.BooleanField(default=True, verbose_name='Recieve Promotional Newsletter Emails?')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agentnotification', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('testimony', models.CharField(blank=True, max_length=400, null=True, verbose_name='Testimony')),
                ('active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usertestimony', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LoginHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='User IP')),
                ('country', models.CharField(max_length=50, null=True, verbose_name='User Country')),
                ('country_flag', models.URLField()),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MinValueValidator(90.0)], verbose_name='Location Latitude')),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MinValueValidator(180.0)], verbose_name='Location Longitude')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Located City')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='Located State')),
                ('language_code', models.CharField(blank=True, max_length=3, null=True, verbose_name='Language Code')),
                ('currency_symbol', models.CharField(blank=True, max_length=10, null=True, verbose_name='Currency Symbol')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loginhistory', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AgentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Company Name')),
                ('company_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Company Address')),
                ('account_number', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Account Number')),
                ('bvn', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Bank Verification Number (BVN)')),
                ('verified', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('bank_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userbank', to='users.banks')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agentprofile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Agent Profile',
                'verbose_name_plural': 'Agent Profiles',
                'ordering': ['user'],
                'managed': True,
            },
        ),
    ]