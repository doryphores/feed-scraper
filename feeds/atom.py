from django.contrib.syndication.views import Feed as FeedView
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404

from feeds.models import Feed


class PodcastFeed(FeedView):
	feed_type = Atom1Feed

	def get_object(self, request, slug):
		return get_object_or_404(Feed, slug=slug)

	def title(self, obj):
		return obj.title

	def link(self, obj):
		return obj.get_absolute_url()

	def items(self, obj):
		return obj.items.all()

	def item_link(self, item):
		return item.get_absolute_url()

	def item_enclosure_url(self, item):
		return item.enclosure

	def item_enclosure_length(self, item):
		return item.length

	def item_pubdate(self, item):
		return item.publish_date

	item_enclosure_mime_type = "audio/mpeg"
