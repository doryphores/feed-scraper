from django.contrib import admin

from feeds.models import *


class FeedAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
admin.site.register(Feed, FeedAdmin)

admin.site.register(Item)
