from django.urls import path

from cars.views import cars

urlpatterns = [
    path('',cars,name='home')
]
