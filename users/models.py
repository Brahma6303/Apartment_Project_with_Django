from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
    
class UserProfile(models.Model):
    age=models.SmallIntegerField()
    mobile_number=models.CharField(max_length=10,default='')
    city=models.CharField(max_length=30,default='')
    country=models.CharField(max_length=30,default='')
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.user.email} ({self.mobile_number}) {self.city} , {self.country})"