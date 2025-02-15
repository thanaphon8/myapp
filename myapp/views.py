from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request, 'home.html')


def navebar(request):
    return render(request, 'nav.html')