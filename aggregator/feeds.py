from django.contrib.syndication.views import Feed

from aggregator.models import Post
from aggregator.settings import NUMBER_OF_POSTS

class LatestPostsFeed(Feed):
    title = "Blogs Nicaragua, Nuestro Diario, Nuestras Voces"
    link = "/feed/"
    description = ""

    def items(self):
        return Post.objects.order_by("-created_at")[:NUMBER_OF_POSTS]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
