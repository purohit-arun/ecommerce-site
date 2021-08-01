from django.urls import path
from . import views

urlpatterns = [
     path('index/', views.index, name='ShopHome'),
     # path('login/', views.login, name='ShopLogin'),
     path('about/', views.about, name='about'),
    
     path('tracker/', views.tracker, name='tracker'),
     path('search/', views.search, name='search'),
     path('products/<int:id>', views.productView, name='productView'),
     path('checkout/', views.checkOut, name='checkOut'),
     path('handlerequest/', views.handlerequest, name='HandleRequest'),

     #Shubham

     path('', views.user_index, name='home'),
     path('home/', views.user_index, name='home'),

     path('register/', views.register, name="register"),
	path('login/', views.login, name="user-login"),
	path('forget_password/', views.forget_password, name="forget-password"),  
     path('change_password/', views.change_password, name="change-password"), 
	path('logout/', views.logout, name="logout"),

     path('contact/', views.contact, name='contact'),
     path('single_product/<int:cid>', views.single_product, name='single-product'),
     path('single_product_details/<int:pid>', views.single_product_details, name='single-product-details'),

    
     
]
 