from django.shortcuts import render
from cars.models import Car

from pages.models import Team

# Create your views here.

def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_at').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_at')
    # search_fields = Car.objects.values_list('model','year','body_style','city').distinct()
    model_search = Car.objects.values_list('model',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    location_search = Car.objects.values_list('city',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    
    context = {
        'teams':team,
        'featured_cars':featured_cars,
        'latest_cars':latest_cars,
        'model_search':model_search,
        'year_search':year_search,
        'location_search':location_search,
        'body_style_search':body_style_search
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




