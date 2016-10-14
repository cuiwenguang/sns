# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('follow_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=50, null=True, blank=True)),
                ('avatar', models.CharField(max_length=255, null=True, blank=True)),
                ('job', models.CharField(max_length=50, null=True, blank=True)),
                ('mobile', models.CharField(max_length=20, null=True, blank=True)),
                ('integral', models.IntegerField(default=0)),
                ('is_temp', models.BooleanField(default=True)),
                ('provider', models.CharField(default=b'local', max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
