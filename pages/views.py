from django.shortcuts import render
from cars.models import Car

from pages.models import Team

# Create your views here.

def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_at').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_at')
    context = {
        'teams':team,
        'featured_cars':featured_cars,
        'latest_cars':latest_cars
    }
    return render(request,'pages/home.html',context)

def about(request):
    team = Team.objects.all()
    context = {
        'teams':team
    }
    return render(request,'pages/about.html',context)

def services(request):
    return render(request,'pages/services.html',{})

def contact(request):
    return render(request,'pages/contact.html',{})




