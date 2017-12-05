# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import temp_list 
from newsfeed.models import Source, Article

def index(request):
	context = {}
	return render(request, 'newsfeed/index.html', context)

def newsfeed(request):
	article_list = temp_list.articles
	for article in article_list:
		article['source_bias'] = float(Source.objects.get(source_id=article['source_id']).score_average)

	article_list.sort(key=lambda article: abs(article['source_bias']))

	context = {
    	'article_list': article_list,
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

