# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from article.models import Article

from datetime import datetime

from django.http import Http404
# Create your views

#def home(request):
#    return HttpResponse("Hello World, Django")

def detail(request, id):
    try:
    	post = Article.objects.get(id=str(id))
    except Article.DoesNotExits:
    	raise Http404
    return render(request, 'post.html', {'post' : post})

#def test(request):
    #return render(request, 'test.html', {'current_time': datetime.now()})

def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})
