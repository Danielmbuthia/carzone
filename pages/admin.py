from django.contrib import admin
from django.utils.html import format_html
from pages.models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumb_nail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.photo.url))
    
    thumb_nail.short_description = 'Photo'
    list_display = ('firstname','thumb_nail','lastname','designation','created_at')
    list_display_links = ['firstname','thumb_nail']
    search_fields= ('firstname','lastname','designation')
    list_filter= ['designation']
    
admin.site.register(Team, TeamAdmin)