from django.urls import path
from accounts.views import dashboard, login, logout,register

urlpatterns = [
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/',logout,name='logout')
]