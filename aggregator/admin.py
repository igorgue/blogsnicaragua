from django.contrib import admin
from aggregator.models import Blog, Post

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'feed_url', 'added_at')
    search_fields = ('title', 'feed_url')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
