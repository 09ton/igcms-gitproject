from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('transparency', views.transparency, name='transparency'),
    path('services', views.services, name='services'),
]
