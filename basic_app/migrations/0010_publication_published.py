# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-23 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_auto_20180523_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]