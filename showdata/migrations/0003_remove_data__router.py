# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 23:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showdata', '0002_auto_20171203_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='_router',
        ),
    ]
