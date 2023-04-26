from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
import datetime
from .models import *
from . utils import cookieCart, cartData, guestOrder
from django.core.exceptions import ObjectDoesNotExist
import os
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required 


# ERROR - DONE
def error(request):
    print("Error 404")
    error_message = "There seems to be an error here"
    return render(request, 'error.html', {"error_message": error_message})
# END OF ERROR - DONE

# ABOUT US
def about_us(request):
    page_name = f"| About Us"
    
    data = cartData(request)
    cartItems = data['cartItems']

    summary = AboutUs.objects.all()

    context = {'summary': summary, 
                'page_name': page_name,
                'cartItems': cartItems, 
                }
    
    return render(request, 'about_us.html', context)
# END OF ABOUT US

# HELP SECTION - DONE
def help(request):
    page_name = f" | Help"
    
    data = cartData(request)
    cartItems = data['cartItems']
    
    help = Help.objects.first()
    context = {'help': help,
                'page_name': page_name,
                'cartItems': cartItems,
                }
    return render(request, 'help.html', context)
# END OF HELP SECTION - DONE


# DASHBOARD

@login_required(login_url='signup')
def dashboard(request):
    products = Product.objects.all()
    blogs = Blog.objects.all()
    
    total_products = Product.objects.count()
    total_blogs = Blog.objects.count()
    context = {
            'products': products, 
            'blogs': blogs,
            'total_products': total_products, 
            "total_blogs": total_blogs,
            }
    return render(request, 'dashboard.html', context)
# END OF DASHBOARD

def index(request):
    products = Product.objects.all()
    blogs = Blog.objects.all()

    data = cartData(request)
    cartItems = data['cartItems']
    
    # Hot Sale Section
    hot_sale_image = Product.objects.get(id=13)
    # End of Hot Sale Section

    context = {'products': products, 
                'blogs': blogs, 
                'cartItems': cartItems,
                'hot_sale_image': hot_sale_image.imageURL,
                }
    return render(request, 'index.html', context)

def contact_us(request):
    page_name = f"| Contact Us"
    context = {'page_name': page_name}
    return render(request, 'contact_us.html', context)

def store(request):
    page_name = f"| Shop"

    data = cartData(request)
    cartItems = data['cartItems']
    
    recent_products = Product.objects.order_by('-pk')
    products = Product.objects.all()
    context = {'products': products, 
                'page_name': page_name,
                'cartItems': cartItems,
                'recent_products': recent_products,
                }
    return render(request, 'store.html', context)

# CART

def cart(request):
    
    page_name = f"| Cart"

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    

    context = {
                'page_name': page_name,
                'items': items,
                'cartItems': cartItems,
                'order': order,
            }
    return render(request, 'cart.html', context)

# END OF CART

# CHECKOUT

def checkout(request):
    
    page_name = f"| Checkout"
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    context = {
                'page_name': page_name,
                'items': items,
                'order': order,
                'cartItems': cartItems,
            }
    return render(request, 'checkout.html', context)

# END OF CHECKOUT


# PRODUCT DETAIL

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    page_name = f"| {product.name}"
    
    data = cartData(request)
    cartItems = data['cartItems']
    shop = product.shop


    # Create a dynamic URL based on the first 5 words of the product name
    words = product.name.split()[:5]
    url_name = '-'.join(words)
    dynamic_url = f"/product/{pk}/{url_name}/"

    colors = Product.objects.values('available_colors').distinct()

    context = {
            'product': product, 
            'page_name': page_name, 
            'dynamic_url': dynamic_url, 
            'shop':shop,
            'colors': colors,
            'cartItems': cartItems,
            }
        
    return render(request, 'product_detail.html', context)
# END OF PRODUCT DETAIL METHOD

def blog_list(request):
    blogs = Blog.objects.all()
    page_name = f"| Blogs"
    return render(request, 'blog_list.html', {'blogs': blogs,
                                                'page_name': page_name
                                                })

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    page_name = f"| {blog.title}"
    context = {'blog': blog, 'page_name': page_name}
    return render(request, 'blog_detail.html', context)
    
def signup(request):
    return render(request, 'signup.html')

# WISHLIST
def wishlist(request):
    products = Product.objects.all()
    total_products = Product.objects.count()
    page_name = f"| Wishlist"
    
    data = cartData(request)
    cartItems = data['cartItems']
    
    
    context = {'products': products, 
                'total_products':total_products,
                'page_name': page_name,
                'cartItems': cartItems,
                }
    return render(request, 'wishlist.html', context)
# END OF WISHLIST


# BRAND
def brands(request):
    page_name = f"| Brands"
    
    data = cartData(request)
    cartItems = data['cartItems']
    
    brands = set(Product.objects.values_list('shop', flat=True))
    context = {'brands': brands, 
                'page_name': page_name,
                'cartItems': cartItems,
                }
    return render(request, 'brands.html', context)
# END OF BRAND

@csrf_exempt
def newsletter(request):
    page_name = f" | Newsletter Subscription"
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if email:
            newsletter_subscriber = Newsletter.objects.create(email=email)
            newsletter_subscriber.save()
            return JsonResponse({'success': True})
        
    return JsonResponse({'success': False})


# cart update item view

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print(f'The product {productId} was {action}ed')
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    product_name = product.name
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
# end of cart update item view

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    
    if request.user.is_authenticated:
        customer = request.user.customer
        data = json.loads(request.body)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = data['form']['total']
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )


    return JsonResponse('Payment submitted!', safe=False)

def addProduct(request):
    
    page_name = f'| Add New Product'
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        shop = request.POST.get('shop', '')
        description = request.POST.get('description', '')
        keywords = request.POST.get('keywords', '')
        image = request.POST.get('image', '')
        price = request.POST.get('price', '')

        product = Product(name=name,
                        shop=shop,
                        description=description,
                        keywords=keywords,
                        image=image,
                        price=price
                    )
        product.save()
    
    context = { 'page_name': page_name}
    return render(request, 'add_product.html', context)