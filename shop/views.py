from typing import OrderedDict
from django.core.checks.messages import Error
from django.shortcuts import render,redirect
from django.http import HttpResponse, response
from .paytm import checksum
import json
from .paytm import checksum
from django.db import models
from .models import Orders, Product, Contact, OrdersUpdate,Customer
from dashboard.models import Slider, Category
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages #Alert Messagefrom 
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib.auth.hashers import check_password, make_password
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
    view_category = Category.objects.all().filter(IsActive=True)
    search_data= request.GET['search']
    if search_data:
        view_product = Product.objects.all().filter(Q (product_name__icontains = search_data) | Q (desc__icontains = search_data) )
    else:
        view_product = Product.objects.all()
        
    return render(request,'shop/search.html',{'view_category':view_category,'view_product':view_product})

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

def register(request):
    view_category = Category.objects.all().filter(IsActive=True)
    fname = ""
    lname = ""
    email = ""
    mob_no = ""
    pwd = ""
    cpwd = ""
    if request.method == "POST":
        postData = request.POST
        fname = postData.get('firstname')
        lname = postData.get('lastname')
        email = postData.get('email')
        mob_no = postData.get('mobile_no')
        pwd = postData.get('password')
        cpwd = postData.get('confirmpassword')

    # error = None
    # if request.method == "POST":
    #     if not fname:
    #         messages.info(request,'First Name Required...!')
    #     elif not lname:
    #         messages.error(request,'Last Name Required...!')
    #     elif not email:
    #         messages.error(request,'Email Required...!')
    #     elif not mob_no:
    #        messages.error(request,'Mobile No. Required...!')
    #     elif not pwd:
    #         messages.error(request,'Password Required...!')
    #     elif not cpwd:
    #         messages.error(request,'Confirm Password Required...!')

    if request.method == "POST":
        if pwd == cpwd:
            encrypte_pwd = make_password(pwd)
            Customer.objects.create(first_name = fname ,last_name = lname ,phone = mob_no  ,email = email ,user_password = encrypte_pwd)
           
            messages.info(request,'You Register Successfully...')
            return render(request,'shop/login.html')
        else:
            messages.error(request ,"Password not matching...")
            return render(request,'shop/register.html')
    else:
        return render(request,'shop/register.html',{'view_category':view_category})

def login(request):
    view_category = Category.objects.all().filter(IsActive=True)
    error_message = None
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        
        #Check Data is Avialable or not.
        customer = None

        try:   
            customer = Customer.objects.get(email = email)
        except ObjectDoesNotExist:
            error_message = 'Please Register then Login...'
            print(error_message)
            return render(request,'shop/login.html',{'error':error_message,'view_category':view_category}) 

        if customer:
            # if pwd != customer.user_password:
            #     error_message = 'Invalid Password...'
            #     return render(request,'shop/login.html',{'error':error_message})
            Check = check_password(pwd,customer.user_password)
            if Check:
                # messages.info(request,'Welcome To RedayMart')
                request.session['customer'] = customer.id
                return redirect('home')
            else:
                error_message = 'Invalid Email and Password...'
                return render(request,'shop/login.html',{'error':error_message})

    else:
         return render(request,'shop/login.html',{'view_category':view_category})

def forget_password(request):
    view_category = Category.objects.all().filter(IsActive=True)
    error_message = None
    if request.method=="POST":
        email = request.POST.get('email')

        try:   
            customer = Customer.objects.get(email = email)
        except ObjectDoesNotExist:
            error_message = 'Please Register then Login...'
            return render(request,'shop/forgot_password.html',{'error':error_message,'view_category':view_category})

        if customer:
            if email == customer.email:
                request.session['customer'] = customer.id
                return redirect('change-password')
            else:
                error_message = 'Email not found...!'
                return render(request,'shop/forgot_password.html',{'error':error_message,'view_category':view_category})
        else:
            error_message = 'Email not found...!'
    return render(request,'shop/forgot_password.html',{'error':error_message,'view_category':view_category}) 

def change_password(request):
    cid = request.session['customer']
    customer = Customer.objects.get(id = cid)

    if request.method == "POST":
        pwd = request.POST.get('NewPassword')
        cpwd = request.POST['RetypePWD']
        error_message = None

        if pwd == cpwd:
            encrypte_pwd = make_password(pwd)
            customer.user_password = encrypte_pwd
            customer.save()
            messages.info(request,'Password Changed Successfully...')
            return redirect('user-login')
        else:
            messages.info(request ,"Password not matching...")
            return redirect('change_password')

    return render(request,'shop/change_password.html',{'customer':customer})    

def logout(request):
    request.session.clear()
    return redirect('home')

def user_index(request):
    view_slider = Slider.objects.all().filter(IsActive=True)
    view_category = Category.objects.all().filter(IsActive=True)
    
    allProds = []
    catProds = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catProds}
   
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
        # params = {'allProds': allProds,'view_slider':view_slider,'view_category':view_category,'Cust_Data':customer}
    
    if request.session.has_key('customer'):
        cid = request.session['customer']
        customer = Customer.objects.get(id=cid)        
        params = {}
        params['allProds']=allProds
        params['view_slider']=view_slider
        params['view_category']=view_category
        params['Cust_Data']=customer
        return render(request, 'shop/home.html', params)
    else:
        params = {}
        params['allProds']=allProds
        params['view_slider']=view_slider
        params['view_category']=view_category
        return render(request, 'shop/home.html', params)
    
def single_product(request,cid):
    if request.method == 'GET':
        view_category = Category.objects.all().filter(IsActive=True)
        view_product = Product.objects.all().filter(category=cid,status=True)
    return render(request,'shop/product_single.html',{'view_category':view_category,'view_product':view_product})

def single_product_details(request, pid):
    if request.method == 'GET':
        view_category = Category.objects.filter(IsActive=True)
        view_product = Product.objects.filter(product_id=pid)
        product = Product.objects.get(product_id=pid)
        category_id = product.category
        product = Product.objects.filter(status=True,category=category_id)
        print(view_product)
    return render(request,'shop/product_single_details.html',{'view_category':view_category,'view_product':view_product,'product':product})