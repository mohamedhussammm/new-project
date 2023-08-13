from django.db import models
from django.contrib.auth.models import User
import uuid



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
      
      
class Cart(models.Model):
     id=models.UUIDField(default=uuid.uuid4,primary_key=True)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     completed=models.BooleanField(default=False)

     def __str__(self):
          return str(self.id)
                  
      
class CartItem(models.Model):
     drink=models.ForeignKey(drinks,on_delete=models.CASCADE,related_name="items")
     cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cartitems")
     quantity=models.IntegerField(default=0)
     def __str__(self):
          return self.drink.name      
      
      
class Checkout(models.Model):
    
    name=models.CharField(max_length=30, primary_key=True)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    components=models.CharField(max_length=100)
    images=models.ImageField(upload_to='photos/%y/%m/%d')
    def __str__(self):
          return self.name
      

                  
      
     
