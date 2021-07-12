from django.urls.conf import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('logout',views.logout, name='logout'),

    path('index/',views.index, name='index'),
    
    path('blogs/',views.blogs, name='blog'),

    path('orders/',views.orders, name='orders'),

    path('contact/',views.contact, name='contact'),

    path('slider',views.slider, name='slider'),
    path('slider_edit/<int:id>',views.slider_edit, name='slider-edit'),
    path('slider_delete/<int:id>',views.slider_delete, name='slider-delete'),

    path('product_add/',views.product_add,name='product-add'),
    path('product_details/',views.product_details, name="product-details"),
    path('product_edit/<int:id>',views.product_edit, name="product-edit"),
    path('product_delete/<int:id>',views.product_delete, name='product-delete'),

    path('category/', views.category, name="category"),
    path('category_edit/<int:id>', views.category_edit, name="category-edit"),
    path('category_delete/<int:id>',views.category_delete, name='category-delete'),

    path('sub_category/', views.sub_category, name='sub-category'),
    path('sub_category_edit/<int:id>',views.sub_category_edit,name='sub-category-edit'),
    path('sub_category_delete/<int:id>',views.sub_category_delete, name='sub-category-delete'),

    path('comingsoon/',views.comingsoon,name='comingsoon'),
]
