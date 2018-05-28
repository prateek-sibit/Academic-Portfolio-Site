# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-23 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0011_publication_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(blank=True, upload_to='student_image')),
                ('name', models.CharField(max_length=256)),
                ('research_area', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=256)),
            ],
        ),
    ]
