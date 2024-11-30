from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request , "all_chai.html")