# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-22 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='publish_date',
            field=models.DateField(),
        ),
    ]
