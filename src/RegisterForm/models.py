from django.db import models
from django import forms


# Create your models here.

class RegisterForm(models.Model):
    name = models.TextField()
    phoneNumber = models.TextField()
    type = models.TextField()
