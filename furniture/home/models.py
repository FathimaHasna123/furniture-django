from django.db import models

# Create your models here.


class Product(models.Model):
   productName = models.CharField(max_length=255,null=True,blank=True)
   price = models.CharField(max_length=255,null=True,blank=True)
   rates = models.CharField(max_length=255,null=True,blank=True)
   image =  models.ImageField(upload_to='product/',null=True,blank=True)


   def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)  
    password = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    
    
    
class Cart(models.Model):
    productName = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    userId = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    quantity =models.IntegerField(null=True,blank=True)
    
    
    
    def __str__(self):
        return self.name   
    
    
class Blog(models.Model):
    image =  models.ImageField(upload_to='blog/',null=True,blank=True)
    header = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    Paragraphs = models.CharField(max_length=255,null=True,blank=True)
    
    
    
    def __str__(self):
        return self.name 
    
    
class Contact(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    message = models.CharField(max_length=255,null=True,blank=True)
    
    
    def __str__(self):
        return self.name     
    
    
class Wishlist(models.Model):
    productName = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True) 
    userId = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    
    def __str__(self):
        return self.name 