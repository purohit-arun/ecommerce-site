from django.contrib import admin
from .models import Category, Slider, Sub_Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Slider)