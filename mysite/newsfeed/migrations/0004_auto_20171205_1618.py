# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 16:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsfeed', '0003_auto_20171201_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='biasscore',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='biasscore',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newsfeed.Article'),
        ),
    ]
