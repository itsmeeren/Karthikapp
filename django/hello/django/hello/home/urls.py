from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static






# using template inheritance we can apply the base template to the all templates we are going to use
urlpatterns = [
    path('', views.index,name='home'),
    path('spoofing', views.spoofing, name='spoofing'),
    path('ip', views.ip, name='Ip'),
    path('mac', views.mac, name='Images'),
    path('randommac', views.randommac, name='Videos'),
    path('help', views.help, name='Contact Us'),
    path('search', views.search, name='Videos'),
    path('search_image/', views.search_image, name='search_image'),
    path('upload/', views.image_upload_view, name='image_upload_view'),
    path('success/', views.success_page, name='success_page'),








]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)