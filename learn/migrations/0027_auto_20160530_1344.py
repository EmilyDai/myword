# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-30 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0026_auto_20160530_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='\u5206\u7c7b'),
        ),
        migrations.AlterField(
            model_name='column',
            name='slug',
            field=models.CharField(db_index=True, max_length=256, unique=True, verbose_name='\u5206\u7c7b\u7f51\u5740'),
        ),
    ]
