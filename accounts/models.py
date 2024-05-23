from django.db import models
from django.contrib.auth.models import User


class banusers(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__ (self):
        return str(self.username)
    

class Image_Users(models.Model):
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user)
    

class Moreinformation(models.Model):
    phonenumber=models.CharField(max_length=12,blank=True,null=True)
    country=models.CharField(max_length=100,blank=True,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    city=models.CharField(max_length=100,blank=True,null=True)
    

