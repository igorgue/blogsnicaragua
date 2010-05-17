from django.db import models

class Blog(models.Model):
    """Blogs the blogs in the aggregator"""
    title = models.CharField(max_length=200, default="Sin Nombre")
    description = models.TextField(null=True, blank=True)
    feed_url = models.URLField(verify_exists=False)
    added_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    """Post for every blog, generated in a cron"""
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=200, default="Sin Titulo")
    content = models.TextField()
    link = models.URLField(unique=True, verify_exists=False)
    created_at = models.DateTimeField(auto_now_add=True)
