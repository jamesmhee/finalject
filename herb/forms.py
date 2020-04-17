from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as U
from .models import User, Image, Order_Product, Payment, Product, Promotion

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta():
        model = User
        fields = ['username','password1', 'password2', 'first_name', 'last_name','email']

class AddproductForm(forms.Form):
    name = forms.CharField(max_length=255)
    picture = forms.FileField()
