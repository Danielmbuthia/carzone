from django.urls import path

from cars.views import cars,car_details

urlpatterns = [
    path('',cars,name='home'),
    path('<int:id>',car_details,name='car_details')
]
