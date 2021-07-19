from django.shortcuts import render
from django.http import HttpResponse, response

# from django.db import models
# from .models import Orders, Product, Contact
# from math import ceil

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')