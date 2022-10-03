from django.shortcuts import render

from pages.models import Team

# Create your views here.

def home(request):
    team = Team.objects.all()
    context = {
        'teams':team
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




