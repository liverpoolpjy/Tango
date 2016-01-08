# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-08 05:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20160108_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 1, 8, 5, 55, 48, 29000, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
