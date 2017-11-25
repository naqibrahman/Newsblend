# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Source(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=30)
    score_count = models.PositiveIntegerField()
    score_sum = models.PositiveIntegerField()
    score_average = models.DecimalField(max_digits=3, decimal_places=2)

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    article_name = models.CharField(max_length=100)
    score_count = models.PositiveIntegerField()
    score_sum = models.PositiveIntegerField()

class BiasScore(models.Model):
    #user = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    score = models.PositiveIntegerField()
    