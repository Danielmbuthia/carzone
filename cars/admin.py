from django.contrib import admin
from django.utils.html import format_html
from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumb_nail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.car_photo.url))
    
    thumb_nail.short_description = 'Photo'
    list_display = ('car_title','thumb_nail','colour','model','year','price','transmition','is_featured')
    list_display_links = ['car_title','thumb_nail']
    search_fields= ('price','car_title','model')
    list_filter= ['price','model','transmition']
    list_editable = ['is_featured']

admin.site.register(Car,CarAdmin)