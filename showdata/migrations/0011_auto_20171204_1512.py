# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showdata', '0010_remove_importdata_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='shui_1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='shui_2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='shui_3',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='wen_1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='wen_2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='wen_3',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='importdata',
            name='file',
            field=models.FileField(upload_to='File', verbose_name='文件'),
        ),
    ]
