# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20161107_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(blank=True, max_length=255, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='landline',
            field=models.CharField(blank=True, max_length=32, verbose_name='landline'),
        ),
        migrations.AlterField(
            model_name='person',
            name='mobile',
            field=models.CharField(blank=True, max_length=32, verbose_name='mobile'),
        ),
    ]
