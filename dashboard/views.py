import os
from django.http import request
from django.shortcuts import redirect, render
from datetime import datetime
from shop.models import Product, Orders, Contact
from .models import Category,Sub_Category,Slider
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required #Login Required for going any page
from django.contrib import messages #Alert Message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django import forms


# Create your views here.
#------------Authantication--------------
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            #messages.info(request,'Invalid !!!')
            return redirect('login')
    else:
        return render(request,'dashboard/admin-login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url="/ap/")
def index(request):
    return render(request,'dashboard/index.html')

@login_required(login_url="/ap/")
def blogs(request):
    return render(request,'dashboard/dashboard-blog.html')

@login_required(login_url="/ap/")
def contact(request):
    contact=Contact.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(contact, 5)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request,'dashboard/contact.html',{'page_obj':page_obj})

#------------Slider--------------

@login_required(login_url="/ap/")
def slider(request):
    #Insert
    if request.method == "POST":
        sname = request.POST.get('slider_name')
        simage= request.FILES['slider_image']        
        stitle = request.POST.get('slider_title')
        sdesc = request.POST.get('slider_description')
        Status = request.POST.get('chk_IsActive')
        if Status=='on':
            isActive='True'
        else:
            isActive='False'
        Slider.objects.create(slider_name = sname, slider_image = simage,title = stitle, desc = sdesc, InsertedDate = datetime.now(),UpdatedDate=datetime.now(), IsActive = isActive)
        messages.success(request,'Inserted Successfully.')
        return redirect('slider')
    else:
        #view
        slider = Slider.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(slider, 3)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return render(request,'dashboard/slider.html',{'page_obj':page_obj})

def slider_edit(request,id):
    slider_update = Slider.objects.get(slider_id = id)
    if request.method == "POST":
        slider_update.slider_name = request.POST.get('slider_name')
        if len(request.FILES) != 0:
            if len(slider_update.slider_image) > 0:
                os.remove(slider_update.slider_image.path)
            slider_update.slider_image = request.FILES['slider_image']
        slider_update.title = request.POST.get('slider_title')
        slider_update.desc = request.POST.get('slider_description')
        slider_update.InsertedDate = datetime.now() #request.POST.get('Inserted_Date')
        slider_update.UpdatedDate = datetime.now()
        
        Status = request.POST.get('chk_IsActive')
        if Status=='on':
            slider_update.IsActive='True'
        else:
            slider_update.IsActive='False'
        
        slider_update.save()
        messages.success(request,"Updated Successfully.")
        return redirect('slider')
    else:
        return render(request,'dashboard/slider_edit.html',{'obj':slider_update})

def slider_delete(request,id):
    slider_delete = Slider.objects.get(slider_id=id)
    slider_delete.delete()
    messages.success(request,'Delted Successfully.')
    return redirect('slider')
#------------Product--------------

@login_required(login_url="/ap/")
def product_add(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    if request.method == "POST":
        pname = request.POST.get('product_name')
        #pdate = datetime.now()
        price = request.POST.get('price')
        pimage= request.FILES['product_image']     
        cid = request.POST.get('product_category')  
        pcategory = Category.objects.get(category_id=cid)
        #psubcategory = requset.POST['product_subcategory']
        pdesc = request.POST.get('product_desc')
        cstatus = request.POST['chk_status']
        if cstatus=='on':
            status='True'
        else:
            status='False'
        Product.objects.create(product_name=pname, published_date=datetime.now(),price=price, category=pcategory, desc=pdesc,imag=pimage,status=status)
        messages.success(request,'Add Product Successfully.')
        return redirect('product-details')
    else:
        return render(request, 'dashboard/product_add.html', {'cobj':category,'scobj':sub_category})

@login_required(login_url="/ap/")
def product_details(request):
    product = Product.objects.all()
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    page = request.GET.get('page', 1)
    print(product.count)
    paginator = Paginator(product, 5)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    return render(request,'dashboard/product_details.html',{'page_obj':page_obj,'cobj':category,'scobj':sub_category})

def product_edit(request,id):
    update_product=Product.objects.get(product_id=id)
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    if request.method == "POST":
        update_product.product_name = request.POST['product_name']
        update_product.published_date = datetime.now()
        update_product.price = request.POST.get('price')
        if len(request.FILES) != 0:
            if len(update_product.imag) > 0:
                os.remove(update_product.imag.path)
            update_product.imag = request.FILES['product_image']
        category_id = request.POST.get('product_category')
        update_product.category = Category.objects.get(category_id=category_id)
        #psubcategory = requset.POST['product_subcategory']
        update_product.desc = request.POST.get('product_desc')
        cstatus = request.POST.get('chk_status')
        if cstatus=='on':
            update_product.status='True'
        else:
            update_product.status='False'

        update_product.save()
        messages.success(request,"Update Product Successfully.")
        return redirect('product-details')
    else:
        return render(request,'dashboard/product_edit.html',{'obj':update_product,'cobj':category,'scobj':sub_category})

def product_delete(request,id):
    delete_product=Product.objects.get(product_id=id)
    delete_product.delete()
    return redirect('product-details')

#------------category--------------

@login_required(login_url="/ap/")
def category(request):
    #add
    if request.method=="POST":
        cname = request.POST['category_name']
        cimage= request.FILES['category_image']  
        cstatus = request.POST['chk_status']
        if cstatus=='on':
            Status='True'
        else:
            Status='False'
        Category.objects.create(category_name=cname,category_image=cimage, IsActive=Status)
        messages.success(request,"Add successfully...")
        return redirect('category')
    else:
        #view
        category = Category.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(category, 5)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return render(request,'dashboard/category.html',{'page_obj':page_obj})

def category_edit(request,id):
    update_category = Category.objects.get(category_id=id)
    if request.method=="POST":
        update_category.category_name = request.POST.get('category_name')
        if len(request.FILES) != 0:
            if len(update_category.category_image) > 0:
                os.remove(update_category.category_image.path)
            update_category.category_image = request.FILES['category_image']
        cstatus = request.POST.get('chk_status')
        if cstatus=='on':
            update_category.IsActive='True'
        else:
            update_category.IsActive='False'

        update_category.save()
        messages.success(request,"Updated Successfully...")
        return redirect('category')
    else:
        return render(request,'dashboard/category_edit.html',{'cobj':update_category})

def category_delete(request,id):
    delete_category = Category.objects.get(category_id=id)
    messages.success(request,"Deleted Successfully.")
    delete_category.delete()
    return redirect('category')

#----------sub_category-------------

@login_required(login_url="/ap/")
def sub_category(request):
    #add
    category = Category.objects.all()
    if request.method=="POST":
        id = request.POST.get('category') #category_id
        print(id)
        cid=Category.objects.get(category_id=id)
        cname = Category.objects.get(category_id=id)
        scname = request.POST.get('sub_category_name')
        scstatus = request.POST.get('chk_status')

        if scstatus=='on':
            Status='True'
        else:
            Status='False'

        Sub_Category.objects.create(sub_category_name=scname,category_id=cid,category_name=cname, IsActive=Status)
        messages.success(request,"Inserted Successfully...")
        return redirect('sub-category') 
    else:
        #view
        sub_category = Sub_Category.objects.all()#.filter(IsActive=True)
        page = request.GET.get('page', 1)
        paginator = Paginator(sub_category, 5)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return render(request,'dashboard/sub_category.html',{'cobj':category,'page_obj':page_obj})

def sub_category_edit(request,id):
    category = Category.objects.all()
    update_subcategory = Sub_Category.objects.get(sub_category_id=id)
    if request.method=="POST":
        id=request.POST.get('category') #category_id
        
        # update_subcategory.category_name = Category.objects.get(category_name=id)
        # update_subcategory.category_name = Category.objects.get(update_subcategory.category_name)
        # update_subcategory.sub_category_name = request.POST.get('sub_category_name')
        # scstatus = request.POST.get('chk_status')

        # if scstatus=='on':
        #      update_subcategory.status='True'
        # else:
        #      update_subcategory.status='False'

        # update_subcategory.save()
        #messages.success(request,"Updated Successfully...")
        return redirect('sub-category')
    else:
        return render(request,'dashboard/sub_category_edit.html',{'cobj':category,'scobj':update_subcategory})

def sub_category_delete(request,id):
    delete_sub_category = Sub_Category.objects.get(sub_category_id=id)
    delete_sub_category.delete()
    return redirect('sub-category')

#-------------orders-------------

@login_required(login_url="/ap/")
def orders(request):
    orders = Orders.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(orders, 5)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request,'dashboard/orders.html',{'page_obj':page_obj})

def comingsoon(requset):
    return render(requset, 'dashboard/comingsoon.html')
