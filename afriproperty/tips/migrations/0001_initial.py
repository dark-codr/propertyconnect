# Generated by Django 3.1.13 on 2021-09-25 13:50

import afriproperty.tips.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=500, null=True, verbose_name='Tip Title')),
                ('slug', models.SlugField(blank=True, max_length=700, null=True, unique=True)),
                ('tip_type', models.CharField(blank=True, choices=[('Blog Post', 'Blog Post'), ('Tip', 'Tip'), ('News Info', 'News Info')], default='Tip', max_length=11, null=True, verbose_name='Tip Type')),
                ('tip_content', tinymce.models.HTMLField()),
                ('approved', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('tip_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipauthor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tip',
                'verbose_name_plural': 'Tips',
                'ordering': ['-created', 'title'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipVideoFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('video', models.FileField(help_text='Your video should be 40Seconds Long, 20MB in size max', upload_to=afriproperty.tips.models.tip_video)),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipvideo', to='tips.tip')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TipImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', models.FileField(upload_to=afriproperty.tips.models.tip_images)),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipimage', to='tips.tip')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
