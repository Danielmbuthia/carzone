from django.contrib import admin

from contacts.models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','car_title','user','car')
    list_display_links = ['first_name','email']
    search_fields= ('email','first_name','user__username','car__car_title')
    
admin.site.register(Contact,ContactAdmin)