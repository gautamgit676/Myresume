from django.urls import path, include
from app.views import *
urlpatterns = [
   
    path('home',home, name='home'),
    path('',basedemo, name='demo'),
    path("pic", upload_photo, name="upload"),
    path("login", login, name="login"), 
    path("signup", signup, name="signup"),
    path("logout", logout, name="logout"),
]




