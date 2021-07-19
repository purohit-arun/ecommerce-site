from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='ShopHome'),
     path('login/', views.login, name='ShopLogin'),
     path('about/', views.about, name='about'),
     path('contact/', views.contact, name='contact'),
     path('tracker/', views.tracker, name='tracker'),
     path('search/', views.search, name='search'),
     path('products/<int:id>', views.productView, name='productView'),
     path('checkout/', views.checkOut, name='checkOut'),
     path('handlerequest/', views.handlerequest, name='HandleRequest'),

     #Shubham

     path('home/', views.user_index, name='home'),
     path('single_product/<int:id>', views.single_product, name='single-product'),

]
 