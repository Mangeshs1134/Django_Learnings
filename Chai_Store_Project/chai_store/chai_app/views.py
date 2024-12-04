from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render , get_list_or_404
from .models import Chai_Variety , Stores
from .forms import ChaiVarietyForm
# Create your views here.

def home(request):
    chais = Chai_Variety.objects.all()
    
    # return render(request , chai)
    return render(request , "all_chai.html" , {"chais": chais})

def chai_detail(request , chai_id):
    chai = get_list_or_404(Chai_Variety , pk=chai_id)
    return render(request , "chai_detail.html", {"chai":chai})

def display_stores(request):
    stores = None
    form = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = Stores.objects.filter(avail= chai_variety)
    else:
        form = ChaiVarietyForm()
        # pass

    return render(request, "stores.html" ,{'form': form , 'stores': stores }, )