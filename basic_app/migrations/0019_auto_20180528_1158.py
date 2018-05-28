# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-28 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0018_auto_20180526_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('UG', 'Undergraduate'), ('PG', 'Post Graduate')], max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('PhD', 'PhD'), ('M.Tech', 'M.Tech'), ('M.Sc', 'M.Sc')], max_length=10),
        ),
    ]