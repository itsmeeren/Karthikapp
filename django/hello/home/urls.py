from django.contrib import admin
from django.urls import path
from . import views






# using template inheritance we can apply the base template to the all templates we are going to use
urlpatterns = [
    path('', views.index,name='home'),
    path('spoofing', views.spoofing, name='spoofing'),
    path('ip', views.ip, name='Ip'),
    path('mac', views.mac, name='mac'),
    path('randommac', views.randommac, name='Randommac'),
    path('help', views.help, name='Contact Us'),
    path('search', views.search, name='Videos'),



]

