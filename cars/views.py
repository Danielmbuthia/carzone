from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from cars.models import Car

# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_at')
    paginator = Paginator(cars,15)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    context = {
        'cars':paged_cars
    }
    return render(request,'cars/cars.html',context)

def car_details(request,id):
    car = get_object_or_404(Car,pk=id)
    context = {
        'car':car
    }
    return render(request,'cars/details.html',context)