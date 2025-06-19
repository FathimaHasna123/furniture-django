"""
URL configuration for furniture project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productApi/', ProductApi.as_view(),name='productApi'),
    path('productApi/<int:id>', ProductApi.as_view(),name='productUpdateApi'),
    path('userApi/', UserApi.as_view(),name='userApi'),
    path('userApi/<int:id>', UserApi.as_view(),name='userUpdateApi'),
    path('cartApi/', CartApi.as_view(),name='cartApi'),
    path('cartApi/<int:id>', CartApi.as_view(),name='cartCreateApi'),
    path('blogApi/' , BlogApi.as_view(),name='blogApi'),
    path('blogApi/<int:id>' , BlogApi.as_view(),name='blogUpdateApi'),
    path('contactApi/' , ContactApi.as_view(),name='contactApi'),
    path('contactApi/' , ContactApi.as_view(),name='contactCreateApi'),
    path('wishlistApi/' , WishlistApi.as_view(),name='wishlistApi'),
    path('wishlistApi/<int:id>' , WishlistApi.as_view(),name='wishlistCreateApi'),
    
    
    

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
