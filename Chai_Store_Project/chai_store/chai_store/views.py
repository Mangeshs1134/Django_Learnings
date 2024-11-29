from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
    return render(request , "layout.html")

def about(request):

    return HttpResponse("<h1>We are at About Page<h1/>")

def contact(request):
    return HttpResponse("<h1>We are at Contact Page<h1/>")
