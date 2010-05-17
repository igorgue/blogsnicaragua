import os

from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # just one for now
    (r'^$', 'aggregator.views.index'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

# django static serve
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'public')}),
    )
