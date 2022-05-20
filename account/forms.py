from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import * 

User = get_user_model

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "gender", "password1", "password2")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
