from pprint import pprint

from django.core.management import setup_environ
import settings

setup_environ(settings)

from aggregator.models import Blog, Post

from libs import feedparser

def add_new_posts(last_updated=None):
    """Run this on a cron"""
    for blog in Blog.objects.all():
        try:
            document = feedparser.parse(blog.feed_url)
        except:
            print "error parsing"
            continue

        if last_updated is None:
            print("- Adding %i articles from %s" % (len(document['entries']), blog.title))

            for entry in document['entries']:
                # now we create a new post
                post = Post()
                post.blog = blog
                post.title = entry['title']

                if 'summary' in entry:
                    post.content = entry['summary']
                if 'content' in entry:
                    post.content = entry['content']

                post.link = entry['link']
                post.save()
            else:
                # TODO: only parse from a date
                pass

def add_list_txt(filename):
    """old list to new db"""
    blogs_txt = open(filename, 'r')

    for entry in blogs_txt:
        feed_url, title = entry.split(',')

        if feed_url.endswith("blogspot.com/"):
            feed_url += "feeds/posts/default?alt=rss"
        elif feed_url.endswith("blogspot.com"):
            feed_url += "/feeds/posts/default?alt=rss"

        blog = Blog()
        blog.title = title
        blog.feed_url = feed_url

        blog.save()

if __name__ == '__main__':
    add_new_posts()
