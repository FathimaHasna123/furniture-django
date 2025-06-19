from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Product
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=User
        fields = '__all__'
                
        
class CartSerializer(serializers.ModelSerializer):
    productName = ProductSerializer()
    userId = UserSerializer()
    class Meta:
        model=Cart
        fields = '__all__'
        
class CartPostSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Cart
        fields = '__all__'
        

class QuantitySerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Cart
        fields = ['quantity']      
        
class QuantityPostSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Cart
        fields = ['quantity']      
        

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields = '__all__'
        
        
class ContactSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Contact
        fields = '__all__'                
                
                
class WishlistSerializer(serializers.ModelSerializer):
    productName = ProductSerializer()
    userId = UserSerializer()
    
    
    class Meta:
        model=Wishlist
        fields = '__all__' 

class WishlistPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wishlist    
        fields = '__all__'                    