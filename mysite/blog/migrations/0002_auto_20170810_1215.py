# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-10 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(default='red', max_length=200),
        ),
    ]
