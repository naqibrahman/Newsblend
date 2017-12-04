# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import temp_list 


def index(request):
    article_list = temp_list.articles
    context = {
        'article_list': article_list,
    }
    return render(request, 'newsfeed/index.html', context)

def profile(request):
	context = {
		'user': request.user,
	}
	return render(request, 'newsfeed/profile.html', context)
