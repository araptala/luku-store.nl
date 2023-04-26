"""lukustore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    # Admin
    path("admin/", admin.site.urls),
    path('', index,name='index'),
    

    # About Us
    path('about_us/', about_us, name='about_us'),
    
    # Contact Us
    path('contact_us/', contact_us, name='contact_us'),
    
    # Products
    path('store/', store, name='store'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    # Updated URL pattern with dynamic_url
    path('product/<int:pk>/<slug:url_name>/', product_detail, name='product_detail_dynamic'),
    
    # Blog
    path('blog/', blog_list, name='blog_list'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
    
    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),
    
    # Sign Up
    path('signup/', signup, name='signup'),

    # Error
    path('error/', error, name='error'),
    
    # Cart
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    
    # Wishlist
    path('wishlist/', wishlist, name='wishlist'),

    # Newsletter
    path('newsletter/', newsletter, name='newsletter'),
    
    # Help
    path('help/', help, name='help'),
    
    # Brands
    path('brands/', brands, name='brands'),
    # path('brand/<str:brand>/', views.brand_products, name='brand_products'),
    
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
    
    path('add_product/', addProduct, name='addProduct'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)