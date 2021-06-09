from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50) 
    category = models.CharField(max_length=70,default="")
    desc = models.CharField( max_length=100)
    price = models.IntegerField(default="0")
    published_date = models.DateTimeField(null=False)
    imag = models.ImageField(upload_to='shop/img', default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    contact_msg_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=70) 
    email = models.CharField(max_length=90,default="")
    subject = models.CharField( max_length=100)
    message = models.CharField( max_length=500)

    def __str__(self):
        return self.contact_name