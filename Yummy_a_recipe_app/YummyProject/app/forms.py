from django import forms
from .models import Yummy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Yummy
        fields = ['recipe_name', 'text',  'images']
        widgets = {
            "recipe_name" : forms.TextInput(attrs={"class" : 'form-control' }),
            "text" : forms.Textarea(attrs={
                "class": "form-control",
                'rows': 5, 
                'cols': 40, 
                'placeholder': 'Write your recipe here...'
                }),
            "images" : forms.FileInput(attrs={"class": "form-control"})
        }

class UserRegistraionForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            "username" : forms.TextInput(attrs={"class" : 'form-control' }),
            "email" : forms.TextInput(attrs={"class": "form-control"}),
            "password1" : forms.TextInput(attrs={"class": "form-control"}),
            "password2" : forms.TextInput(attrs={"class": "form-control"}),
            # "image" : forms.FileInput(attrs={"class": "form-control"})
        }

        