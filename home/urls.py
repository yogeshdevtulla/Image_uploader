from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
  
    path('', views.upload_image, name='upload-image'),
    path('api/images/', views.images.as_view(), name='image-list'),
    

]