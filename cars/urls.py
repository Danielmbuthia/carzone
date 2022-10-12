from django.urls import path

from cars.views import cars,car_details,car_search

urlpatterns = [
    path('',cars,name='home'),
    path('<int:id>',car_details,name='car_details'),
    path('search',car_search,name='car_search')
]
