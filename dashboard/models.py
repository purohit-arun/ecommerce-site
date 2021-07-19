from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50,default="")
    category_image = models.ImageField(upload_to='dashboard/category',default="")
    IsActive = models.BooleanField(default=1)
    
    def __str__(self) :
        return self.category_name

class Sub_Category(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=50,default="")
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50,default="")
    IsActive = models.BooleanField(default=1)

    def __str__(self) :
        return self.sub_category_name

class Slider(models.Model):
    slider_id = models.AutoField(primary_key=True)
    slider_name = models.CharField(max_length=100)
    slider_image = models.ImageField(upload_to='dashboard/slider',default="")
    title = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=200,default="")
    InsertedDate = models.DateTimeField(null=False)
    UpdatedDate = models.DateTimeField(null=False)
    IsActive = models.BooleanField(default=1)

    def __str__(self):
        return self.slider_name