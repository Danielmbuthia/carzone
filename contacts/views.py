import imp
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.contrib import messages
from cars.models import Car
from contacts.models import Contact
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car = Car.objects.get(pk=request.POST['car'])
        if Contact.objects.filter(
            car=request.POST['car'],
            user=request.POST['user']   
        ).exists():
            messages.info(request,'You have an enquiry of this car')
            return redirect("cars:car_details",id=car.id)
        else:
            user = User.objects.get(pk=request.POST['user'])
            contact = Contact.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                user = user,
                car = car,
                email = request.POST['email'],
                message = request.POST['message'],
                customer_need = request.POST['customer_need'],
                car_title = request.POST['car_title'],
                city = request.POST['city'],
                state = request.POST['first_name'],
                phone = request.POST['phone'],
            )
            admin_info = User.objects.get(is_superuser=True)
            admin_email = admin_info.email
            send_mail(
                'New Car Inquery',
                f"{request.POST['first_name']} is requesting about a car '{request.POST['car_title']}'. PLease Login to admin for more info",
                request.POST['email'],
                [admin_email,'contact@carzone.com'],
                fail_silently=True,
            )
            contact.save()
            messages.success(request,'Thank you for reaching to us we will respond to you shortly ')
            return redirect("cars:car_details",id=car.id)

        
        
def contact(request):
     if request.method == 'POST':
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            request.POST['subject'],
            f" Customer {request.POST['name']} using phone {request.POST['phone']} has sent this message.\n\n {request.POST['message']}.",
            request.POST['email'],
            [admin_email,'contact@carzone.com'],
            fail_silently=True,
        )
        messages.success(request,'Thank you for reaching to us we will respond to you shortly ')
        return redirect("pages:contact")