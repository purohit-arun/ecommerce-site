from django.urls import path
from . import views

urlpatterns = [
     path('index/', views.index, name='ShopHome'),
     path('login/', views.login, name='ShopLogin'),
     path('about/', views.about, name='about'),
     path('shop/contact/', views.contact, name='contact'),
     path('tracker/', views.tracker, name='tracker'),
     path('search/', views.search, name='search'),
     path('products/<int:id>', views.productView, name='productView'),
     path('checkout/', views.checkOut, name='checkOut'),
     path('handlerequest/', views.handlerequest, name='HandleRequest'),

     #Shubham

     path('', views.user_index, name='home'),
     path('shop/home/', views.user_index, name='home'),
     path('shop/single_product/<int:cid>', views.single_product, name='single-product'),
     path('shop/single_product_details/<int:pid>', views.single_product_details, name='single-product-details'),

]
 