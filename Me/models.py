from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserDataBase(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    profile_title = models.CharField(max_length=200, null=True, blank=True)
    tweeter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)



class   Education(models.Model):
    user=models.ForeignKey(UserDataBase,on_delete=models.CASCADE,null=True,blank=True)
    count_edu=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    admission_date= models.DateField(null=True, blank=True)
    graduate_date = models.DateField(null=True, blank=True)
    result=models.CharField(max_length=200,null=True,blank=True)
    about=models.TextField(max_length=200, null=True, blank=True)

