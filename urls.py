from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('feeds.urls')),
)

# Serve static and media files in DEBUG mode
# In production, these files will be served by the web server
if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
