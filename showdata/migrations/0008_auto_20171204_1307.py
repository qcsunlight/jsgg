# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 13:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showdata', '0007_auto_20171203_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='info',
        ),
        migrations.RemoveField(
            model_name='data',
            name='kong',
        ),
        migrations.RemoveField(
            model_name='data',
            name='router',
        ),
        migrations.RemoveField(
            model_name='data',
            name='state',
        ),
        migrations.RemoveField(
            model_name='data',
            name='volt',
        ),
    ]