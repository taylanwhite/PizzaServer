# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-30 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0008_auto_20170130_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietaryrestrictions',
            name='veggieToppings',
            field=models.ManyToManyField(blank=True, default='VeggieTopping', to='quickstart.VeggieTopping'),
        ),
    ]