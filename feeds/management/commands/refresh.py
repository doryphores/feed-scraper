from django.core.management.base import BaseCommand
from feeds.models import Feed


class Command(BaseCommand):
	help = 'Refreshes all feeds'

	def handle(self, *args, **options):
		for feed in Feed.objects.all():
			feed.scrape(True)
