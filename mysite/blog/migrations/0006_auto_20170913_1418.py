# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-13 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170913_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='address1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='resume',
            name='address2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experiance',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='resume',
            name='hobbies',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='resume',
            name='qualification',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
