from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
ACCOUNT_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('customrer', 'Customer'),
        ('employee', 'Employee')
    )
class User(AbstractUser):
    role=models.CharField(choices=ACCOUNT_TYPE_CHOICES,max_length=50,null=True)