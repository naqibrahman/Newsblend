# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.cache import cache
from django_redis import get_redis_connection

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import temp_list
from django.contrib.auth.models import User
from newsfeed.models import Source, Article, BiasScore
from scraper import scrape
import json

def index(request):
	context = {}
	return render(request, 'newsfeed/index.html', context)

def newsfeed(request):
	article_list = temp_list.articles
	for article in article_list:
		article['source_bias'] = float(Source.objects.get(source_id=article['source_id']).score_average)
	#	article['text']= "".join(scrape(article["url"]))
	# for artice in article_list:
	# 	##IF in memcache: export it
	# 	#else:
	# 
	article_list.sort(key=lambda article: abs(article['source_bias']))

	r = get_redis_connection("default")
	articles = r.lrange("articles", 0, -1)
	for i in range(0, len(articles)):
		articles[i] = json.loads(articles[i])
	
	articles.sort(key=lambda article: abs(article['source_bias']))

	context = {
    	'article_list': articles,
    }
	
	return render(request, 'newsfeed/newsfeed.html', context)

def profile(request):
	context = {
		'user': request.user,
	}
	return render(request, 'newsfeed/profile.html', context)

def news_page(request, article):
	print(article)
	context = {}
	return render(request, 'newsfeed/news_page.html', context)

def article(request, articleId):
	r = get_redis_connection("default")
	articles = r.lrange("articles", 0, -1)
	for i in range(0, len(articles)):
		articles[i] = json.loads(articles[i])

	article_url = filter( lambda article: article["id"] == int(articleId), articles)[0]['url']
	article_content = r.lrange(article_url, 0, -1)
	if not article_content:
		article_content = scrape(article_url)
		r.lpush(article_url, *article_content)
		r.expire(article_url, 300)
	return HttpResponse(article_content)

def create_bias_score(request):
	if request.method == 'POST':
		score = request.POST.get('score')
		article_id = request.POST.get('articleid')
		current_user = request.user
		user = User.objects.get(id=current_user.id)
		article = Article.objects.get(article_id=article_id)
		bias_score = BiasScore(score=score)
		bias_score.user = user
		bias_score.article = article
		bias_score.save()

		"""
		TODO redesign model or do these writes somewhere else to reduce number of writes per POST
		"""
		article.score_count = article.score_count + 1
		article.score_sum = article.score_sum + int(score)
		article.save()

		source = article.source
		source.score_count = source.score_count + 1
		source.score_sum = source.score_sum + int(score)
		source.score_average = source.score_sum / source.score_count
		source.save()
		return HttpResponse("test")
