# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juntagrico', '0003_auto_20171013_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='amount',
            field=models.FloatField(default=1.0, verbose_name='Wert'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='multiplier',
            field=models.PositiveIntegerField(
                default=1, verbose_name='Arbeitseinsätze vielfaches'),
        ),
    ]
