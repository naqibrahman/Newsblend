# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import services


def index(request):
    services.get_headlines()
    return HttpResponse("Hello, world. You're at the newsfeed index.")