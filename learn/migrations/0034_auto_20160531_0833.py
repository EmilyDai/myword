# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-31 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0033_auto_20160530_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='daka',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
