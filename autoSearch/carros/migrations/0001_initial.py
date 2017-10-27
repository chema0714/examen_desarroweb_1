# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 23:17
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('created', models.CharField(default=b'16:17 PM', max_length=100)),
            ],
        ),
    ]