# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0004_auto_20171214_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='score_sum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='source',
            name='score_sum',
            field=models.IntegerField(default=0),
        ),
    ]