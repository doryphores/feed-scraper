from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from feeds.models import *

from feeds.atom import PodcastFeed

urlpatterns = patterns('',
	url(r'^$', ListView.as_view(model=Feed), name='feed_list'),
	url(r'^(?P<slug>[-_\w]+)/$', DetailView.as_view(model=Feed), name='feed_details'),
	url(r'^(?P<slug>[-_\w]+)/(?P<pk>\d+)/$', DetailView.as_view(model=Item), name='item_details'),
	url(r'^(?P<slug>[-_\w]+)/feed/$', PodcastFeed(), name='feed_feed'),
)
