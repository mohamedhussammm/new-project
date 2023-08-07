from operator import truediv
from pickle import TRUE
from django.db import models

class signuppage(models.Model):
     
     firstname=models.CharField(max_length=20)
     lastname=models.CharField(max_length=20)
     username=models.CharField(unique=True, max_length=20,null=True,blank=TRUE)
     phonenumber=models.CharField(max_length=20)
     email=models.CharField(unique=True, max_length=20)
     password=models.CharField(max_length=20)
     cpassword=models.CharField(max_length=20)
     nationalid=models.ImageField(upload_to='photos/%y/%m/%d',null=True,blank=TRUE)
     picture=models.ImageField(upload_to='photos/%y/%m/%d',null=True,blank=TRUE)
     active=models.BooleanField(default=True)
     def __str__(self):
        return self.firstname
     
 

