# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.cache import cache
from django_redis import get_redis_connection

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from newsfeed.models import Source, Article, BiasScore
from scraper import scrape
import json

def index(request):
    """
    Renders index page
    """
    context = {}
    return render(request, 'newsfeed/index.html', context)

def newsfeed(request):
    """
    Renders newsfeed page
    Retrieves article headlines from Redis instance
    """
    r = get_redis_connection("default")
    articles = r.lrange("articles", 0, -1)
    for i in range(0, len(articles)):
        articles[i] = json.loads(articles[i])
    context = {
        'article_list': articles,
    }	
    return render(request, 'newsfeed/newsfeed.html', context)

def profile(request):
    """
    Renders profile page
    """
    context = {
        'user': request.user,
    }
    return render(request, 'newsfeed/profile.html', context)

def article(request, articleId):
    """
    Renders article page
    Checks if article text is already in Redis
    If not in Redis, stored in Redis for 5 minutes
    """
    r = get_redis_connection("default")
    articles = r.lrange("articles", 0, -1)
    for i in range(0, len(articles)):
        articles[i] = json.loads(articles[i])

    article_url = filter(lambda article: article["id"] == int(articleId), articles)[0]['url'] #finds which article to render
    article_content = r.lrange(article_url, 0, -1)
    if not article_content:
        article_content = scrape(article_url)
        r.lpush(article_url, *article_content)
        r.expire(article_url, 300)
    return HttpResponse(article_content)

def create_bias_score(request):
    """
    Writes user submitted bias score to database
    """
    if request.method == 'POST':
        score = request.POST.get('score')
        article_id = request.POST.get('articleid')
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        article_obj = Article.objects.get(article_id=article_id)
        bias_score = BiasScore(score=score)
        bias_score.user = user
        bias_score.article = article_obj
        bias_score.save()

        """
        TODO redesign model or do these writes somewhere else to reduce number of writes per POST
        """
        article_obj.score_count = article_obj.score_count + 1
        article_obj.score_sum = article_obj.score_sum + int(score)
        article_obj.save()

        source = article_obj.source
        source.score_count = source.score_count + 1
        source.score_sum = source.score_sum + int(score)
        source.score_average = source.score_sum / source.score_count
        source.save()
        return HttpResponse("test")
