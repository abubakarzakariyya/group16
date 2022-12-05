from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('service/', service, name='services'),
    #path('contact/', contact, name='contact'),
    path('teams/', teams, name='teams'),
    path('gallery-single/', gallery_single, name='gallery-single'),
    path('people/', all_request, name= 'details'),
    path('photos/<int:id>/photo/details/', details, name='photo-details'),
    path('create/', contact_view, name='contact')
]