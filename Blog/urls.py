"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('blogapp.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

]
