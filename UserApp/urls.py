from django.urls import path
from  . import views
from .froms import LoginForm
urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),
    path("customer/",views.CustomerView.as_view(),name="customer"),
    path("admin/",views.AdminView.as_view(),name="admin"),
    path("employee/",views.EmployeeView.as_view(),name="employee"),
    path('login/',views.CustomLoginView.as_view(),name='login'),    
    path("signup/",views.SignupView.as_view(),name="signup"),

]