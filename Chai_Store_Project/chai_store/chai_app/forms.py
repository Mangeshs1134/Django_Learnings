from django import forms
from .models import Chai_Variety

class ChaiVarietyForm (forms.Form):

    chai_variety = forms.ModelChoiceField(queryset=Chai_Variety.objects.all(), label="Select Chai Variety : ")
    