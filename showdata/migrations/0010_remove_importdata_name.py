# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 13:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showdata', '0009_auto_20171204_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importdata',
            name='name',
        ),
    ]
