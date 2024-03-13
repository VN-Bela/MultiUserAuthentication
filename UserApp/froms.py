from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import User
class LoginForm(AuthenticationForm): 
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password =forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class SignUpForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 =forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password1 =forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=("username","password1","password2","role")