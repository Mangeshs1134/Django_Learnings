from django import forms
from .models import Yummy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Yummy
        fields = ['text', 'images']

class UserRegistraionForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')