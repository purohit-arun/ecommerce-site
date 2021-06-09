# ecommerce-site
Django project

Before working on this project create a branch and then do your work 
In this the ecart folder is main project and shop and blog are two apps 


-->tutorial for you
for opening the python shell for database query (django ORM feature)
step 1: open cmd typed python manage.py shell
step 2: import models that you want to query upon 
i.e from shop.modesl import Product or to import all models of
any app type from shop.models import *

if your want something like this "select * from product where category='Electronics' " than write the following command in shell 
Product.objects.filter(category = "Electronics")

to get fiels along with columns --> Product._meta.fields