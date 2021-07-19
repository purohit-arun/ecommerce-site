from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('single_blog/<int:id>', views.single_blog, name="single-blog"),
    path('blogpost/<int:id>', views.blogpost, name="BlogPost"),
]
