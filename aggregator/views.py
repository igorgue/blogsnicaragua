from django.shortcuts import render_to_response

from aggregator.settings import *
from aggregator.models import Blog, Post

from libs import feedparser

def index(request):
    """This gets the last NUMBER_OF_POSTS"""
    posts = Post.objects.all().order_by('-created_at')[:NUMBER_OF_POSTS]

    return render_to_response('temp_index.html', locals())
