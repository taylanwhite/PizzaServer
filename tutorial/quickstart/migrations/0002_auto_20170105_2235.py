# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-05 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedpizza',
            name='extra',
            field=models.ManyToManyField(blank=True, default='Extra', to='quickstart.Extra'),
        ),
        migrations.AlterField(
            model_name='orderedpizza',
            name='meatToppings',
            field=models.ManyToManyField(blank=True, default='MeatTopping', to='quickstart.MeatTopping'),
        ),
        migrations.AlterField(
            model_name='orderedpizza',
            name='veggieToppings',
            field=models.ManyToManyField(blank=True, default='VeggieTopping', to='quickstart.VeggieTopping'),
        ),
        migrations.AlterField(
            model_name='specialtypizza',
            name='meatToppings',
            field=models.ManyToManyField(blank=True, default='MeatTopping', to='quickstart.MeatTopping'),
        ),
        migrations.AlterField(
            model_name='specialtypizza',
            name='veggieToppings',
            field=models.ManyToManyField(blank=True, default='VeggieTopping', to='quickstart.VeggieTopping'),
        ),
    ]
