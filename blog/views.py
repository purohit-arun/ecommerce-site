from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
from dashboard.models import Category


# Create your views here.

def blog(request):
    myposts = Blogpost.objects.all()
    view_category = Category.objects.all().filter(IsActive=True)
    return render(request, 'blog/blog.html',{'myposts' : myposts,'view_category':view_category})

def blogpost(request, id):
    post = Blogpost.objects.filter(blog_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',{ 'post' : post})

def single_blog(request,id):
    single_post = Blogpost.objects.filter(blog_id = id)[0]
    view_category = Category.objects.all().filter(IsActive=True)
    return render(request, 'blog/single_blog.html',{'post' : single_post,'view_category':view_category})
