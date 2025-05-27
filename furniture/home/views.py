from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.



class  ProductApi(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        print("get method called")
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id=None):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        product = Product.objects.get(id=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
    
    
class UserApi(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)  
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        user = User.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
    
    
class CartApi(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self,request,id=None):
        cart = Cart.objects.get(id=id)
        serializer = CartSerializer(cart,data=request.data)
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        cart = Cart.objects.get(id=id)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
class BlogApi(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id=None):
        blog = Blog.objects.get(id=id)
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        blog = Blog.objects.get(id=id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
class ContactApi(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class WishlistApi(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        wishlist = Wishlist.objects.all()
        serializer = WishlistSerializer(wishlist,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = WishlistPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
    
    def put(self,request,id=None):
        wishlist = Wishlist.objects.get(id=id)
        serializer = WishlistPostSerializer(wishlist,data=request.data)
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        wishlist = Wishlist.objects.get(id=id)
        wishlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
         
