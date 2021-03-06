"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from herb import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.my_homepage, name='myhomepage'),
    path('index/', views.index, name='index'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('register/', views.my_register, name='register'),
    path('myaccount/', views.my_account, name='myaccount'),
    path('changepassword/', views.change_mypassword, name='changepassword'),
    path('createproduct/', views.create_product, name='createproduct'),
    path('editprofile/<int:pro_id>', views.edit_profile, name='editprofile'),
    path('product/<int:pro_id>', views.look_product, name='product'),
    path('mycart/<int:pro_id>', views.my_cart, name='mycart'),
    path('editproduct/<int:pro_id>', views.edit_product, name='editproduct'),
    path('delproduct/<int:pro_id>', views.del_product, name='delproduct'),
    path('promtion/', views.my_promotion, name='promotion'),
    path('orderprofile/<int:pro_id>', views.order_profile, name='orderprofile'),
    path('createpromotions/', views.create_promotions, name='createpromotions'),
    path('editpromotions/<int:pro_id>', views.edit_promotions, name='editpromotions'),
]

# urlpatterns += staticfiles_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)