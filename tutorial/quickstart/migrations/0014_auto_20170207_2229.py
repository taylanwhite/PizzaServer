# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-07 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0013_auto_20170207_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietaryrestrictionslist',
            name='crustType',
            field=models.ManyToManyField(blank=True, default='CrustType', to='quickstart.CrustType'),
        ),
    ]
