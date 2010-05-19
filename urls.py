import os

from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from aggregator.feeds import LatestPostsFeed

urlpatterns = patterns('',
    # just one for now
    (r'^$', 'aggregator.views.index'),

    # feeds
    (r'^feeds/$', LatestPostsFeed()),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

# django static serve
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^images/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'public/images')}),
            (r'^javascripts/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'public/javascripts')}),
            (r'^stylesheets/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'public/stylesheets')}),
    )
