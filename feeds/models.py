import datetime
import urllib2
from email.utils import parsedate_tz
import re
from BeautifulSoup import BeautifulSoup as BSoup

from django.db import models
from django.core.files.storage import default_storage as storage
from django.core.files.base import ContentFile
from django.utils.timezone import utc

from feeds import utils


class Feed(models.Model):
	title = models.CharField(max_length=400)
	slug = models.SlugField(max_length=400)
	page_url = models.URLField(max_length=400)
	parser = models.TextField(max_length=400)
	updated_date = models.DateTimeField(auto_now=True)

	def scrape(self, force=False):
		html = self.download(force)

		# Parse HTML
		html_soup = BSoup(html)

		for link in html_soup.body.findAll(href=re.compile('\.mp3$')):
			enclosure = link['href']
			if not self.items.filter(enclosure=enclosure).exists():
				item = Item(title=link.text.strip(), enclosure=link['href'])
				item.get_info()
				self.items.add(item)

	def download(self, force=False):
		file_name = '%s.html' % self.slug

		if force or not storage.exists(file_name):
			f = urllib2.urlopen(self.page_url)
			html = f.read()

			# Write it to disk
			storage.save('%s.html' % self.slug, ContentFile(html))
		else:
			# Read HTML
			with storage.open(file_name) as f:
				html = f.read()

		return html

	@models.permalink
	def get_absolute_url(self):
		return ('feed_details', (), {
			'slug': self.slug,
		})

	def __unicode__(self):
		return u'%s' % self.title

	class Meta:
		ordering = ['-updated_date']
		get_latest_by = 'updated_date'


class Item(models.Model):
	title = models.CharField(max_length=400)
	enclosure = models.URLField(max_length=400)
	length = models.PositiveIntegerField(default=0)
	feed = models.ForeignKey(Feed, related_name='items')
	publish_date = models.DateTimeField()
	updated_date = models.DateTimeField(auto_now=True)

	def get_info(self):
		headers = utils.get_headers(self.enclosure)
		self.length = headers['Content-Length']
		lm_tuple = parsedate_tz(headers['Last-Modified'])
		self.publish_date = datetime.datetime(*lm_tuple[0:6]).replace(tzinfo=utc)

	@models.permalink
	def get_absolute_url(self):
		return ('item_details', (), {
			'slug': self.feed.slug,
			'pk': self.pk,
		})

	def __unicode__(self):
		return u'%s' % self.title

	class Meta:
		ordering = ['-publish_date']
