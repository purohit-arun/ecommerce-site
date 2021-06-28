from typing import OrderedDict
from django.shortcuts import render
from django.http import HttpResponse

from django.db import models
from .models import Orders, Product, Contact
from math import ceil

# Create your views here.


def index(request):
    """ products = Product.objects.all()
    print(products) """
    allProds = []
    print('Product all prods', allProds, '\n')
    catProds = Product.objects.values('category', 'product_id')
    print('Printing catProds', catProds, '\n')
    cats = {item['category'] for item in catProds}
    print("Printing cats", cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        print(n)
        nSlides = n//4 + ceil((n/4) - (n//4))
        print(nSlides)
        print(prod)
        allProds.append([prod, range(1, nSlides), nSlides])
    """ params = {
        'no_of_slides': nSlides,
        'range': range(1, nSlides),
        'product': products
    } """
    """ allProds=[[products, range(1, nSlides), nSlides],
            [products, range(1, nSlides), nSlides]] """
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def login(request):
    return render(request, 'shop/login.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(contact_name=name, email=email,
                          subject=subject, message=message)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, id):
    # Fetch the product using the id
    product = Product.objects.filter(product_id=id)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkOut(request):
    if request.method == "POST":
        name = request.POST.get('inputname')
        email = request.POST.get('inputEmail4')
        address = request.POST.get('inputAddress')
        city = request.POST.get('inputCity')
        state = request.POST.get('state')
        zip_code = request.POST.get('inputZip')
        phone = request.POST.get('phone')
        order = Orders(name=name, email=email, address=address,
                       city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank' : thank, 'id' : id})    
    return render(request, 'shop/checkout.html')
