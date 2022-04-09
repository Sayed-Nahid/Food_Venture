from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dev_info', views.dev_info, name='dev_info'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('showdata', views.showdata, name='showdata'),
]