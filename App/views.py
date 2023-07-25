from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . models import Category, Varieties, Disease, Symptoms,CropCategory
from . models import ProductCategory, CropVarieties, ProductVarieties 
from django . http import JsonResponse
import json


# Create your views here.

def index(request):
    return render(request, 'html/index.html')

def signup(request):
    
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not lastname or not firstname or not username or not email or not password:
            print("Incomplete details")
        else:
            new_user = User.objects.create(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
            new_user.save()
            return redirect('home')
    return render(request, 'html/signup.html')

def login(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username is None or password is None:
            messages.info(request, 'username or password not found')
            return redirect('/login')
        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'Invalid login credentials')
            return redirect('/login')
        auth.login(request, user)
        return redirect('home')
    return render(request, 'html/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return render (request, 'html/about.html')

def service(request):
    return render(request, 'html/services.html')

def home(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'html/home.html', context)


def market(request):
    category = ProductCategory.objects.all()
    context = {
        'category': category
    }
    
    return render(request, 'html/market.html', context)


def varieties(request, id):
    cat = Category.objects.get(id = id)
    category = Varieties.objects.filter(category = cat)
    context = {"category": category, "name":cat.name }
    return render (request, 'html/varieties.html', context)


def read(request, id):
    variety = Varieties.objects.get(id=id)
    diseases = Disease.objects.filter(varieties = variety)
    context = {"variety": variety, "diseases": diseases}
    return render (request, 'html/read.html', context)


def crop(request):
    category = CropCategory.objects.all()
    context = {
        'category': category
    }
    return render(request, 'html/crop.html', context)


def crops(request, id):
    cat = CropCategory.objects.get(id = id)
    category = CropVarieties.objects.filter(category = cat)
    context = {"category": category, "name":cat.name }
    return render (request, 'html/cropvarieties.html', context)


def readcrops(request, id):
    variety = CropVarieties.objects.get(id=id)
    # diseases = Disease.objects.filter(varieties = variety)
    context = {"variety": variety}
    return render (request, 'html/readcrops.html', context)


def products(request, id):
    cat = ProductCategory.objects.get(id = id)
    category = ProductVarieties.objects.filter(category = cat)
    context = {"category": category, "name":cat.name }
    return render (request, 'html/productvarieties.html', context)


def readproduct(request, id):
    variety = ProductVarieties.objects.get(id=id)
    context = {"variety": variety}
    return render (request, 'html/readproduct.html', context)


def cart (request):
    # customer = request.user.customer
    # order, created = order.objects.get_or_create(customer=customer, complete=False)
    return render(request, 'html/cart.html')



def checkout (request):
    return render(request, 'html/checkout.html')


def payment (request):
    return render(request, 'html/payment.html')

# def updateItems (request):
#     data = json.loads(request.data)
#     productId = ['productId']
#     action = data ['action']

#     print('action:', action)
#     print('productId', productId)

#     customer = request.user.customer
#     product = products.objects.get(id=productId)

#     order, created = order.objects.get_or_create(customer=customer, complete=False)
#     orderItem = orderItem.objects.get_or_created(order=order, product=product)

#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity +1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity -1)

#     orderItem.save()

#     if orderItem.quantity <= 0:
#         orderItem.delete()
#     return JsonResponse ('Item was added', safe=False)