# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'verbose_name': '\u9891\u9053', 'verbose_name_plural': '\u9891\u9053'},
        ),
        migrations.AlterField(
            model_name='channel',
            name='channel_name',
            field=models.CharField(max_length=20, verbose_name='\u9891\u9053\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='cover_img',
            field=models.CharField(max_length=255, null=True, verbose_name='\u9891\u9053\u56fe\u7247', blank=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='order_index',
            field=models.IntegerField(default=0, verbose_name='\u6392\u5e8f'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='parent_id',
            field=models.IntegerField(default=0, verbose_name='\u7236\u7ea7'),
        ),
    ]
