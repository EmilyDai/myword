# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-30 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0031_auto_20160530_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='column',
            field=models.CharField(default='\u516d\u7ea7', max_length=256, unique=True),
        ),
    ]
