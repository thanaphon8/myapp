from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('nav', views.navebar, name='nav'),
]