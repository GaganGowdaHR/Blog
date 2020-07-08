from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group 
from django.contrib.auth.models import User


# Create your models here.


# 1. Create a new model and add User model as one to one field 
# 2. inherit AbstarctUser Model






class User(AbstractUser):
    email = models.EmailField(unique = True)
    bio = models.CharField(max_length=500,blank = True)
    image = models.ImageField(upload_to="profile/",blank = True)
    is_author = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    bio = models.CharField(max_length=500,blank = True)
    image = models.ImageField(upload_to="profile/",blank = True)

    def __str__(self):
        return self.user.username




