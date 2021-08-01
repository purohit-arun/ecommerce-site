from django.db import models
from dashboard.models import Category
# Create your models here.


class Customer(models.Model):
        first_name = models.CharField(max_length=200, null=True, default="")
        last_name = models.CharField(max_length=200, null=True, default="")
        phone = models.CharField(max_length=200, null=True,default="")
        email = models.CharField(max_length=200, null=True,default="")
        user_password = models.CharField(max_length=20,default="")
        date_created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
            return self.email

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    desc = models.CharField( max_length=100)
    price = models.IntegerField(default="0")
    published_date = models.DateTimeField(null=False)
    status = models.BooleanField(default=1)
    imag = models.ImageField(upload_to='shop/img', default="")

    def __str__(self):
        return self.product_name

    @staticmethod
    def get_productby_id(id):
        return Product.objects.filter(product_id__in=id)

    @staticmethod
    def get_all_product_by_category_id(cid):
        if cid:
            return Product.objects.filter(category = cid)
        else:
            return Product.objects.all()

class Contact(models.Model):
    contact_msg_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=70) 
    email = models.CharField(max_length=90,default="")
    subject = models.CharField( max_length=100)
    message = models.CharField( max_length=500)

    def __str__(self):
        return self.contact_name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(max_length=100, default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=90)
    state = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    phone = models.IntegerField()

class OrdersUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."


