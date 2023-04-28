

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Ecommerce(models.Model):
    
    Name = models.CharField(max_length=255)
    price = models.CharField(max_length=25)

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    

    # def __str__(self):
    #     return self.Name