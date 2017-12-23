# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_addr', models.CharField(max_length=15)),
                ('_name', models.CharField(max_length=15)),
                ('_time', models.CharField(max_length=20)),
                ('_state', models.CharField(max_length=15)),
                ('_info', models.CharField(max_length=15)),
                ('_volt', models.CharField(max_length=15)),
                ('_kong', models.CharField(max_length=10)),
                ('_router', models.CharField(max_length=15)),
            ],
        ),
    ]
