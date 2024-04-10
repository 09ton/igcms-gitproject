from django.contrib import admin
from .models import Related
from django.utils.html import format_html

class RelatedAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 2px;" />'.format(object.event_photo.url))

    thumbnail.short_description = 'Photo'


    list_display = ('id', 'thumbnail', 'title', 'held_in', 'held_on')
    list_display_links = ('id', 'thumbnail', 'title',)
    search_fields = ('title', 'held_in', 'held_on')

admin.site.register(Related, RelatedAdmin)
