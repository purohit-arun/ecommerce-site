from django.contrib import admin
from .models import OrdersUpdate, Product, Contact, Orders, Customer
# Register your models here.

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrdersUpdate)
admin.site.register(Customer)


