from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'dashboard/admin-login.html')

def index(request):
    return render(request,'dashboard/index.html')

def blogs(request):
    return render(request,'dashboard/dashboard-blog.html')

def orders(request):
    return render(request,'dashboard/orders.html')

def add_product(requset):
    return render(requset, 'dashboard/add_product.html')

def comingsoon(requset):
    return render(requset, 'dashboard/comingsoon.html')