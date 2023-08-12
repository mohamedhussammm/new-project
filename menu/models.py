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
      
      
      
     
<<<<<<< HEAD
=======
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(items,drinks,lunch,dinner,composes, on_delete=models.CASCADE)  # Assuming you have a Product model      
>>>>>>> 1bc5eedfcc148ecd0e19860fdcb93b6e20e22a29
      

                  
      
     
