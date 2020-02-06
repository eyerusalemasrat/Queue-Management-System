from django.db import models

# Create your models here.
class RegisterForm(models.Model):
    
    name = models.TextField()
    phoneNumber = models.TextField()
    Residential = models.TextField()
    Enterprise = models.TextField()