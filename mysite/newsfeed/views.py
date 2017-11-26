# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import services
import temp_list 


def index(request):
    #services.get_headlines()
    print temp_list.articles
    return HttpResponse("Hello, world. You're at the newsfeed index.")