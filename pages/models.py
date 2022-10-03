from django.db import models

# Create your models here.

class Team(models.Model):
    firstname = models.CharField(max_length =255)
    lastname = models.CharField(max_length =255)
    designation = models.CharField(max_length =255)
    photo = models.ImageField(upload_to='photos/team/')
    facebook_link = models.URLField(max_length=100, null=True, blank=True)
    twitter_link = models.URLField(max_length=100, null=True, blank=True)
    google_plus_link = models.URLField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    ordering = ['created_at']
    def __str__(self):
        return self.firstname
        