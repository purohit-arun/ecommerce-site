from django.shortcuts import render
from django.http import HttpResponse

from django.db import models
from .models import Product
from math import ceil

# Create your views here.


def index(request):
    """ products = Product.objects.all()
    print(products) """
    allProds = []
    print(allProds)
    catProds = Product.objects.values('category','product_id')
    print(catProds)
    cats = {item['category'] for item in catProds}
    print("Printing cats",cats)
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    """ params = {
        'no_of_slides': nSlides,
        'range': range(1, nSlides),
        'product': products
    } """
    """ allProds=[[products, range(1, nSlides), nSlides],
            [products, range(1, nSlides), nSlides]] """
    params={'allProds':allProds }
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def login(request):
    return render(request, 'shop/login.html')


def contact(request):
    return render(request, 'shop/index.html')


def tracker(request):
    return render(request, 'shop/index.html')


def search(request):
    return render(request, 'shop/index.html')


def productView(request):
    return render(request, 'shop/index.html')


def checkOut(request):
    return render(request, 'shop/index.html')
