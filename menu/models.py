from django.db import models
from django.contrib.auth.models import User



class items(models.Model):
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    components=models.CharField(max_length=100)
    images=models.ImageField(upload_to='photos/%y/%m/%d')
    def __str__(self):
          return self.name
      
      
      
class drinks(models.Model):
    
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    components=models.CharField(max_length=100)
    images=models.ImageField(upload_to='photos/%y/%m/%d')
    def __str__(self):
          return self.name
      
      
class lunch(models.Model):
    
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    components=models.CharField(max_length=100)
    images=models.ImageField(upload_to='photos/%y/%m/%d')
    def __str__(self):
          return self.name      
      
class dinner(models.Model):
    
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    components=models.CharField(max_length=100)
    images=models.ImageField(upload_to='photos/%y/%m/%d')
    def __str__(self):
          return self.name   
      
      
class composes(models.Model):
    
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    components=models.CharField(max_length=100)
    images=models.ImageField(upload_to='photos/%y/%m/%d')
    def __str__(self):
          return self.name  
      
      
      
class Checkout(models.Model):
    
    name=models.CharField(max_length=30, primary_key=True)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    components=models.CharField(max_length=100)
    images=models.ImageField(upload_to='photos/%y/%m/%d')
    def __str__(self):
          return self.name
      

                  
      
     
