from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .froms import LoginForm,SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import User


# Create your views here.
class IndexView(generic.TemplateView):
    template_name="registration/index.html"
    
class AdminView(generic.TemplateView):
    template_name="UserApp/admin.html"
class CustomerView(generic.TemplateView):
    template_name="UserApp/customer.html"
class EmployeeView(generic.TemplateView):
    template_name="UserApp/employee.html"

class SignupView(generic.CreateView):
    template_name="registration/signup.html"
    form_class=SignUpForm
    success_url=reverse_lazy("login")

class  CustomLoginView(generic.FormView):
    template_name="registration/login.html"
    form_class=AuthenticationForm
    success_url=reverse_lazy("index")
    model=User

    def form_valid(self, form) :
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(self.request,user)
            if user.role=="admin":
                self.success_url=reverse_lazy("admin")
            elif user.role=="customer":
                self.success_url=reverse_lazy("customer")
            elif user.role=="employee":
                self.success_url=reverse_lazy("employee")
            return super().form_valid(form)
        else:
            form.add_error(None,"Invalid username and password")
            return self.form_invalid(form)
