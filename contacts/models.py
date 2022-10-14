
import datetime
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from cars.models import Car

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    customer_need = models.CharField(max_length=500)
    car_title = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    phone = models.CharField(max_length=100,blank=True)
    message =  RichTextField(blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)