from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from contacts.models import Contact

# Create your views here.
def login(request):
    if request.method == 'POST':
        password = request.POST['Password']
        username = request.POST['username']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request,f'{username} welcome back')
            return redirect("accounts:dashboard")
        messages.error(request,'An issue with your login credentials')
    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('accounts:register') 
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already exists")
                    return redirect('accounts:register') 
                else:
                    user = User.objects.create_user(
                        first_name = firstname,
                        last_name = lastname,
                        username = username,
                        password = password,
                        email=email
                    )
                    auth.login(request,user)
                    messages.success(request,f'{username} welcome on board')
                    return redirect('accounts:dashboard')
        else:
            messages.error(request,'password mismatch')
            return redirect('accounts:register')         
    return render(request,'accounts/register.html')

@login_required(login_url='/accounts/login/')
def dashboard(request):
    car_inqueries = Contact.objects.order_by('-created_at').filter(user_id=request.user.id)
    context = {
        'inqueries':car_inqueries
    }
    print(context)
    return render(request,'accounts/dashboard.html',context)

def logout(request):
    auth_logout(request)
    return redirect('pages:home')

