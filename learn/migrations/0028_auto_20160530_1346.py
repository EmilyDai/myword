# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-30 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0027_auto_20160530_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='\u529f\u80fd'),
        ),
        migrations.AlterField(
            model_name='function',
            name='slug',
            field=models.CharField(db_index=True, max_length=256, unique=True, verbose_name='\u529f\u80fd\u7f51\u5740'),
        ),
    ]
