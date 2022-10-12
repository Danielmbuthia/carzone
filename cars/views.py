from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from cars.models import Car

# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_at')
    paginator = Paginator(cars,5)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    location_search = Car.objects.values_list('city',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    

    context = {
        'cars':paged_cars,
        'model_search':model_search,
        'year_search':year_search,
        'location_search':location_search,
        'body_style_search':body_style_search
    }
    return render(request,'cars/cars.html',context)

def car_details(request,id):
    car = get_object_or_404(Car,pk=id)
    context = {
        'car':car
    }
    return render(request,'cars/details.html',context)

def car_search(request):
    model_search = Car.objects.values_list('model',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    location_search = Car.objects.values_list('city',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search = Car.objects.values_list('transmition',flat=True).distinct()
    cars = Car.objects.order_by('-created_at')
    if 'keyword' in request.GET:
        cars = cars.filter(
            car_title__icontains=request.GET.get('keyword')
        )
    if 'select_type' in request.GET:
        cars = cars.filter(
            body_style__iexact=request.GET.get('select_type')
        )
    if 'select_make' in request.GET:
        cars = cars.filter(
            model__icontains=request.GET.get('select_make')
    )
    if 'select_year' in request.GET:
        cars = cars.filter(
            year__iexact=request.GET.get('select_year')
        )
    if 'select_location' in request.GET:
        cars = cars.filter(
            state__iexact=request.GET.get('select_location'),
            city__icontains = request.GET.get('select_location')
        )
    if 'transmission' in request.GET:
        cars = cars.filter(
            transmition__iexact=request.GET.get('transmission')
        )
        
    if 'min_price' in request.GET:
        cars = cars.filter(price__gte=request.GET.get('min_price'),price__lte=request.GET.get('max_price'))
    context = {
        'cars':cars,
        'model_search':model_search,
        'year_search':year_search,
        'location_search':location_search,
        'body_style_search':body_style_search,
        'transmission_search':transmission_search
    }
    return render(request,'cars/car_search.html',context)