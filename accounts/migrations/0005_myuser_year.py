# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-06 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_myuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='year',
            field=models.CharField(default='1', max_length=40, verbose_name='Name'),
        ),
    ]