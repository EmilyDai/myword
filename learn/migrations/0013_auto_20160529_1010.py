# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-29 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0012_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.AddField(
            model_name='user',
            name='column',
            field=models.ManyToManyField(default='', to='learn.Column', verbose_name='\u9009\u62e9\u5206\u7c7b'),
        ),
    ]
