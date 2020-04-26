from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.fields import TextField

from .models import (Image, Order_Item, Order_Product, Payment, Product,
                     Promotion, Order)
from .models import User as U


class CreateUserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1', 'password2', 'first_name', 'last_name','email']

class AddproductForm(forms.Form):
    name = forms.CharField()
    picture = forms.FileField()

class AdditemForm(forms.Form):
    quanlity = forms.FloatField()
    

class AddorderForm(forms.Form):
    class Meta():
        model = Order
    # items = forms.IntegerField() 
    # total_price = forms.FloatField()
    # delivery_location = forms.CharField(widget=forms.Textarea)

class AddpromotionsForm(forms.Form):
    name = forms.CharField()
    
