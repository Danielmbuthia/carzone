from django.urls import path

from contacts.views import inquiry,contact
urlpatterns = [
    path('',inquiry,name='inquiry_create'),
    path('contacts/',contact,name='contact')
]
