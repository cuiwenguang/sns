# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('channel_id', models.IntegerField()),
                ('cover', models.CharField(max_length=500)),
                ('template', models.IntegerField()),
                ('remark', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('is_original', models.BooleanField(default=False)),
                ('source', models.CharField(max_length=50)),
                ('user_id', models.IntegerField(default=0)),
                ('user_name', models.CharField(max_length=50, null=True, blank=True)),
                ('user_avatar', models.CharField(max_length=255)),
                ('status', models.IntegerField(default=0)),
                ('comment_num', models.IntegerField(default=0)),
                ('agree_num', models.IntegerField(default=0)),
                ('page_url', models.CharField(max_length=500)),
                ('update_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel_name', models.CharField(max_length=20)),
                ('cover_img', models.CharField(max_length=255)),
                ('order_index', models.IntegerField(default=0)),
                ('parent_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_content', models.CharField(max_length=255)),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=50)),
                ('user_avatar', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('agree_num', models.IntegerField(default=0)),
                ('article_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('user_name', models.CharField(max_length=50, null=True, blank=True)),
                ('article_id', models.IntegerField()),
                ('collect_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('user_name', models.CharField(max_length=50, null=True, blank=True)),
                ('channel_id', models.IntegerField()),
                ('channel_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_id', models.IntegerField()),
                ('tag_words', models.CharField(max_length=50)),
            ],
        ),
    ]
