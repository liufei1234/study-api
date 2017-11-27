# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('car_status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'car',
                'managed': False,
            },
        ),
    ]