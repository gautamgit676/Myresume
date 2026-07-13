from django.urls import path, include
from app.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
   
    path('home',home, name='home'),
    path('',basedemo, name='demo'),
    path("pic", upload_photo, name="upload"),
    path("login", loginuser, name="login"), 
    path("signup", signup, name="signup"),
    path("logout", logoutuser, name="logout"),
    path("resume", myresume, name="resume"),
    path("clickphoto", clickphoto, name="clickphoto"),
    
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset_form.html"
        ),
        name="password_reset",
    ),
    
    path( "password-reset/done/", auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done", ),
    
    path( "reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",),
    
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",),
    
    
]
    





