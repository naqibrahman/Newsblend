# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#class UserProfile(models.Model):
#user = models.OneToOneField(User, unique=true)

class Source(models.Model):
    source_id = models.CharField(max_length=30, primary_key=True)
    source_name = models.CharField(max_length=30)
    score_count = models.PositiveIntegerField(default=0)
    score_sum = models.PositiveIntegerField(default=0)
    score_average = models.DecimalField(max_digits=3, decimal_places=2, default=0)

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    article_name = models.CharField(max_length=300)
    score_count = models.PositiveIntegerField(default=0)
    score_sum = models.PositiveIntegerField(default=0)

class BiasScore(models.Model):
    user = models.ForeignKey(User, null=True)
    article = models.ForeignKey(Article, null=True)
    score = models.IntegerField()
