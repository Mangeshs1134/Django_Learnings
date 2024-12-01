from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render , get_list_or_404
from .models import Chai_Variety
# Create your views here.

def home(request):
    chais = Chai_Variety.objects.all()
    
    # return render(request , chai)
    return render(request , "all_chai.html" , {"chais": chais})

def chai_detail(request , chai_id):
    chai = get_list_or_404(Chai_Variety , pk=chai_id)
    return render(request , "chai_detail.html", {"chai":chai})