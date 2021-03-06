# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_log_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logcompanymentions',
            name='log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='logs.Log'),
        ),
        migrations.AlterField(
            model_name='logpersonmentions',
            name='log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people', to='logs.Log'),
        ),
    ]
