from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta:
		model = Customer
		# fields = ['username', 'email', 'password1', 'password2']
		fields = ['name']
		print(f"{type(fields)}{fields}")

