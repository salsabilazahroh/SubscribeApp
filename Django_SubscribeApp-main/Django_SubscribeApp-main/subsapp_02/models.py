from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)