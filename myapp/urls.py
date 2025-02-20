# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.aboutPage, name='about'),  # นี่คือ URL ของ 'about'
    path('property/', views.propertiesPage, name='property'),
    path('contact/', views.contactPage, name='contact'),
    path('owner/', views.ownerPage, name='owner'),
    path('tenant/', views.tenant_view, name='tenant'),
    path('lease/', views.leasePage, name='lease'),
]
