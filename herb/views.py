from builtins import object
from fnmatch import filter
from http.client import HTTPResponse
from logging import warning
from os.path import supports_unicode_filenames
from tokenize import group
from urllib.request import Request
from venv import create

from astroid import objects
from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import Group, Permission, User
from django.contrib.messages.api import success
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.template.context_processors import request
from pkg_resources import require

from isort.utils import difference

from .forms import AdditemForm, AddproductForm, CreateUserForm
from .models import (Image, Order_Item, Order_Product, Payment, Product,
                     Promotion)
from .models import User as U


# Create your views here.
def my_homepage(request):
    return redirect('index')

def index(request):
    product_all = Product.objects.all()
    userapp = request.user.id
    userappinfo = User.objects.all()
    # search = request.GET.get('searchbox')
    # product_list = Product.objects.filter(name=search)
    # if search != '' and search is not None:
    #     product_list = Product.objects.filter(name=search)
    #     return redirect('product/')
    # # image_all = Image.objects.get(pk=Product.id) 
    # context = {'product':product_list, 'searchbox': search, 'product_all':product_all}
    context = {'product_all':product_all, 'userapp':userapp, 'userappinfo': userappinfo}

    return render(request, 'index.html', context)

def my_login(request): #หน้าสมัครสมาชิกและล็อกอิน
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, 'ชื่อผู้ใช้งาน หรือ รหัสผ่าน ไม่ถูกต้อง หรือ ไม่มีในระบบ')
    
    context = {}

    return render(request, "login.html", context=context)
    
@login_required(login_url='login')
def my_logout(request):
    logout(request)
    return redirect('login')


def my_register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='user')
                user.groups.add(group)               
                messages.success(request, 'สมัครสมาชิกเรียบร้อย')
            else:
                messages.warning(request, 'สมัครสมาชิกไม่สำเร็จ เนื่องจาก Username หรือ Email นี้มีในระบบอยู่แล้ว หรือ รหัสผ่านไม่ตรงตามเงื่อนไข')
                return redirect('register')

    context = {'form':form}
    return render(request, "register.html", context)

@login_required
def change_mypassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'เปลี่ยนรหัสผ่านใหม่เรียบร้อย')
            return redirect('changepassword')
        else:
            messages.warning(request, 'รหัสผ่านปัจจุบันผิด หรือ รหัสไม่ตรงกัน หรือ ไม่ตรงตามเงื่อนไข')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}    
    return render(request, 'changepassword.html', context)
    
@login_required
@permission_required('product.add_product')
def create_product(request):
    if request.method == 'POST':
        form = AddproductForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Product(name = request.POST['name'], quanlity = request.POST['quanlity'],
            price = request.POST['price'],
            picture = request.FILES['picture'])
            newdoc.save()
        # if request.POST.get('name') and request.POST.get('quanlity') and request.POST.get('price') and request.FILES.get('picture'):
        #     product=Product()
        #     product.name = request.POST.get('name')
        #     product.quanlity = request.POST.get('quanlity')
        #     product.price = request.POST.get('price')
        #     product.picture = request.FILES.get('picture')
        #     product.save()
            return redirect('index')
    else:
        form = AddproductForm()
    return render(request, "createproduct.html", {'form':form})

@login_required
@permission_required('product.edit_product')
def edit_product(request, pro_id):
    context = {}
    product_all = Product.objects.get(pk=pro_id)
    if request.method == 'POST':
        product_all.name = request.POST['name']
        product_all.quanlity = request.POST['quanlity']
        product_all.price = request.POST['price']
        product_all.save()
        return redirect('index')

    context['product_all'] = product_all

    return render(request, 'editproduct.html', context)

def edit_profile(request, pro_id):
    context = {}
    my_doc = User.objects.get(pk=pro_id)
    if request.method == 'POST':
        my_doc.email = request.POST['email']
        my_doc.first_name = request.POST['first_name']
        my_doc.last_name = request.POST['last_name']
        my_doc.save()
    context['my_doc'] = my_doc
    return render(request, 'editprofile.html', context=context)

@login_required
@permission_required('product.delete_product')
def del_product(request, pro_id):
    context = {}
    product_all = Product.objects.all()
    product_del = Product.objects.get(id=pro_id)
    if request.method == 'POST':
        product_del = Product.objects.get(id=pro_id)
        product_del.delete()
        return redirect('index')
    context['product_all'] = product_all 
    context['product_del'] = product_del 
    return render(request, 'delproduct.html', context)

def look_product(request, pro_id):
    producttotal = Product.objects.get(id=pro_id)
    context = {'producttotal': producttotal}
    return render(request, 'product.html', context)

def my_cart(request, pro_id):
    context = {}
    cart = []
    productone = Product.objects.all()
    productid = pro_id
    # if request.method == 'POST':
    #     form = AdditemForm(request.POST)
    #     if form.is_valid():
    #         newcart = Order_Item(quanlity = request.POST['quanlity'], buy_by_user = User.objects.get(username=request.user.username))
    #         newcart.save()
    #     return redirect('mycart')
    context['productid'] = productid
    context['productone'] = productone
    # context['productall'] = productall
    return render(request, 'mycart.html', context)


# def add_to_cart(request, slug):
#     item = get_object_or_404(Product, slug=slug)
#     order_item, created = Order_Item.objects.get_or_create(
#         item=item,
#         user=request.user,
#         ordered=False
#     )
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item.quantity += 1
#             order_item.save()
#             messages.info(request, "Item qty was updated.")
#             return redirect("index")
#         else:
#             order.items.add(order_item)
#             messages.info(request, "Item was added to your cart.")
#             return redirect("index")
#     else:
#         ordered_date = timezone.now()
#         order = Order.objects.create(
#             user=request.user, ordered_date=ordered_date)
#         order.items.add(order_item)
#         messages.info(request, "Item was added to your cart.")
#     return render(request, 'mycart.html')

def buy_item(request, pro_id):
    context = {}

    return render(request, 'order.html', context)


def my_promotion(request):
    context = {}
    promotion_all = Promotion.objects.all()

    context['promotion_all'] = promotion_all
    return render(request, 'promotion.html', context)
