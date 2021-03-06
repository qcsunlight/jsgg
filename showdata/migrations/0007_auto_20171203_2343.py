# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 23:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showdata', '0006_auto_20171203_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='_01addr',
            new_name='addr',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_02name',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_13kong',
            new_name='kong',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_10state',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_11info',
            new_name='router',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_04shui_1',
            new_name='shui_1',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_05wen_1',
            new_name='shui_2',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_06shui_2',
            new_name='shui_3',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_12volt',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_03time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_14router',
            new_name='volt',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_07wen_2',
            new_name='wen_1',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_08shui_3',
            new_name='wen_2',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='_09wen_3',
            new_name='wen_3',
        ),
    ]
