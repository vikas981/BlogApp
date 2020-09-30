
from django.urls import path
from blogapp.views import (homepage, register,
                           login_app, logout_from_app,
                           single_slug)

app_name = 'blogapp'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('register', register, name='register'),
    path('login', login_app, name='login'),
    path('logout', logout_from_app, name='logout'),
    path('<single_slug>', single_slug, name="single_slug"),

]
