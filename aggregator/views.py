from django.shortcuts import render_to_response

from aggregator.settings import *
from aggregator.models import Blog, Post

from libs import feedparser

def index(request):
    """This gets the last NUMBER_OF_POSTS"""
    posts = dict()

    def add_post(post):
        """add a post to the dict"""
        date = str(post.created_at.date())
        if not date in posts:
            posts[date] = []
            posts[date].append(post)
        else:
            posts[date].append(post)

    map(add_post, Post.objects.order_by('-created_at')[:NUMBER_OF_POSTS])
    blogs = Blog.objects.all()

    return render_to_response('index.html', {'posts': posts, 'blogs': blogs})
