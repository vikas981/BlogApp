"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blogapp import views

router = DefaultRouter()
router.register("BlogCategory", views.blogcategoryapi)
router.register("BlogSeries", views.blogsriesapi)
router.register("Blog", views.blogapi)

urlpatterns = [
    path('', include('blogapp.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

]
