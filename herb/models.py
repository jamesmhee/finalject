from django import forms
from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as U
from django.db import models
from setuptools.command.upload import upload

PAYMENT_STATUS = {
        ('AR' ,'Arrived'),
        ('NA' ,'Not_Arrived')
    }

END_PROMOTION = {
        ('S', 'SALE'),
        ('NS', 'NOTSALE')
    }
# Create your models here.
class User(models.Model):
   username = models.CharField(max_length=255)
   password = models.CharField(max_length=255)
   first_name = models.CharField(max_length=255)
   last_name = models.CharField(max_length=255)
   email = models.EmailField()

def __str__(self):
    return self.username


class Product(models.Model): # สินค้า
    name = models.CharField(max_length=255)
    quanlity = models.IntegerField(default=1)
    price = models.FloatField()
    picture = models.FileField(upload_to='documents/%Y/%m/%d')
    # slug = models.SlugField()

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=255)
    discount = models.IntegerField()
    end_promotion = models.CharField(choices=END_PROMOTION, max_length=2)

class Image(models.Model):
    image = models.FileField(upload_to='documents/%Y/%m/%d')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order_Item(models.Model): #รายการสินค้า
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quanlity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.quanlity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quanlity * self.item.price

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    items = models.ForeignKey(Order_Item, on_delete=models.CASCADE)        
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    ordered_date = models.DateTimeField()

    delivery_location = models.TextField(blank=True)
    total_price = models.FloatField()
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=2)
    # user_id = models.ForeignKey(U, on_delete=models.CASCADE)
    promotion_id = models.ForeignKey(Promotion, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Payment(models.Model):
    date = models.DateField(null=True, blank=True)
    upload = models.CharField(max_length=255)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

class Order_Product(models.Model):
    unit = models.IntegerField()
    unit_price = models.FloatField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)    
