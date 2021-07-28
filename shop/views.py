from typing import OrderedDict
from django.shortcuts import render,redirect
from django.http import HttpResponse, response
import json
from .paytm import checksum
from django.db import models
from .models import Orders, Product, Contact, OrdersUpdate,Customer
from dashboard.models import Slider, Category
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages #Alert Message

# Create your views here.
MERCHANT_KEY = 'Dt_Y#CKJYVa%NKUH'


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
    thank = False
    view_category = Category.objects.all().filter(IsActive=True)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(contact_name=name, email=email,
                          subject=subject, message=message)
        contact.save()
        thank = True
        messages.success(request,'Thank for contacting us')
    return render(request, 'shop/contact.html', {'thank': thank,'view_category':view_category})

def tracker(request):
    if request.method == "POST":
        orderID = request.POST.get('orderId')
        email = request.POST.get('email')
        try:
            order = Orders.objects.filter(order_id=orderID, email=email)
            print("This is order id for tracking", order, "email", email)
            if len(order) > 0:
                update = OrdersUpdate.objects.filter(order_id=orderID)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(
                        [updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, id):
    # Fetch the product using the id
    product = Product.objects.filter(product_id=id)
    return render(request, 'shop/productview.html', {'product': product[0]})

def checkOut(request):
    if request.method == "POST":
        items_json = request.POST.get('itemJson')
        name = request.POST.get('inputname')
        amount = request.POST.get('amount')
        email = request.POST.get('inputEmail4')
        address = request.POST.get('inputAddress')
        city = request.POST.get('inputCity')
        state = request.POST.get('state')
        zip_code = request.POST.get('inputZip')
        phone = request.POST.get('phone')
        order = Orders(items_json=items_json, amount=amount, name=name, email=email, address=address,
                       city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrdersUpdate(order_id=order.order_id,
                              update_desc="Order Placed Successfully")
        update.save()
        amount = float(amount)
        print(f'float -> {amount}')
        thank = True
        id = order.order_id
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {
            'MID': 'pPzDap69091253306077',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})
        # return render(request, 'shop/checkout.html', {'thank' : thank, 'id' : id})
    return render(request, 'shop/checkout.html')

# for handling the paytm payment request

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            Checksumm = form[i]

    verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, Checksumm)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})


def user_index(request):
    view_slider = Slider.objects.all().filter(IsActive=True)
    view_category = Category.objects.all().filter(IsActive=True)

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
        params = {'allProds': allProds,'view_slider':view_slider,'view_category':view_category}
    return render(request, 'shop/home.html', params)
    # return render(request,'shop/home.html',{'view_slider':view_slider,'view_category':view_category})

def single_product(request,cid):
    if request.method == 'GET':
        view_category = Category.objects.all().filter(IsActive=True)
        view_product = Product.objects.all().filter(category=cid,status=True)
    return render(request,'shop/product_single.html',{'view_category':view_category,'view_product':view_product})

def single_product_details(request, pid):
    if request.method == 'GET':
        view_category = Category.objects.all().filter(IsActive=True)
        view_product = Product.objects.all().filter(product_id=pid)
        product = Product.objects.all().filter(status=True)
        print(view_product)
    return render(request,'shop/product_single_details.html',{'view_category':view_category,'view_product':view_product,'product':product})