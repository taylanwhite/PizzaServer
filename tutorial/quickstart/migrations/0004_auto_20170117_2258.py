# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-17 22:58
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20170106_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedpizza',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5),
        ),
        migrations.AlterField(
            model_name='orderedpizza',
            name='status',
            field=models.ManyToManyField(blank=True, default='Status', to='quickstart.Status'),
        ),
    ]
