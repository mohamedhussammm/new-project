from django.db import models
class photos(models.Model):
 firstimage=models.ImageField(null=True, blank=True, upload_to='photos/%y/%m/%d')
 secondimage=models.ImageField(null=True, blank=True,upload_to='photos/%y/%m/%d')
 thirdimage=models.ImageField(null=True, blank=True,upload_to='photos/%y/%m/%d')
 fourthimage=models.ImageField(null=True, blank=True, upload_to='photos/%y/%m/%d')
 fifthimage=models.ImageField(null=True, blank=True,upload_to='photos/%y/%m/%d')
 sixthimage=models.ImageField(null=True, blank=True,upload_to='photos/%y/%m/%d')

