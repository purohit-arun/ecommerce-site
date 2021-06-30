from django.urls.conf import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('index/',views.index, name='index'),
    path('blogs/',views.blogs, name='blog'),
    path('orders/',views.orders, name='orders'),
    path('add_product/',views.add_product,name='add-product'),
    path('comingsoon/',views.comingsoon,name='comingsoon')
]
