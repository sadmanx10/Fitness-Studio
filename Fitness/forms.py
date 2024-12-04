from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class ProductForm(ModelForm):
   class Meta:
       model = Productz
       fields = ['name', 'category', 'price', 'stock_quantity', 'description', 'rating','image']

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'username', 'email', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['title', 'description', 'details', 'image']

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'title', 'image', 'bio']