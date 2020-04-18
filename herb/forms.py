from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image, Order_Product, Payment, Product, Promotion, Order_Item
from .models import User as U
class CreateUserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1', 'password2', 'first_name', 'last_name','email']

class AddproductForm(forms.Form):
    name = forms.CharField(max_length=255)
    picture = forms.FileField()

class AdditemForm(forms.Form):
    quanlity = forms.FloatField()
    