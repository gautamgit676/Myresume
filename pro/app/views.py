from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Photo
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from app.task import send_welcome_email
from django_ratelimit.decorators import ratelimit


# Create your views here.


# @ratelimit(key='ip', rate='10/h', method='GET', block=True)# if need for custome spasific cache use this 
# @ratelimit(key='ip', rate='10/h', method='POST', block=True)# if need for custome spasific cache use this 
def  home(request):
    return render(request , 'home.html')

def  basedemo(request):
    return render(request , 'base.html')

def myresume(request):
    return render(request , 'resume.html')

def clickphoto(request):
    if request.method=="POST":

        title=request.POST.get("title")

        image=request.FILES.get("image")

        Photo.objects.create(

            title=title,

            image=image

        )

        return redirect("clickphoto")

    photos=Photo.objects.all()

    return render(request,"reals.html",{ "photos":photos})
    # return render(request , 'reals.html')



def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("signup")

        user = User.objects.create_user(username=username,email=email,password=password)
        messages.success(request, "Account created successfully. Please login.")
        send_welcome_email.delay(user.email, user.username)
        return redirect("login")

    return render(request, "signup.html")



def logoutuser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def upload_photo(request):

    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")
        user = request.user  # Get the currently logged-in user

        # ❌ 1. Check empty upload
        if not image:
            messages.error(request, "Please select an image")
            return redirect("upload")

        # ❌ 2. File size limit (5MB example)
        if image.size > 5 * 1024 * 1024:
            messages.error(request, "Image must be under 5MB")
            return redirect("upload")

        # ✅ Save safely
        Photo.objects.create(
            title=title,
            image=image,
            user=user
        )

        messages.success(request, "Photo uploaded successfully!")
        return redirect("upload")

    photos = Photo.objects.filter(user=request.user).order_by("-id")  # Show latest first
    return render(request, "pics.html", {"photos": photos})

