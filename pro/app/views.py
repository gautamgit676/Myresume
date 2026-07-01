from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Photo
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.



def  home(request):
    return render(request , 'home.html')

def  basedemo(request):
    return render(request , 'base.html')


def login(request):
    return render(request , 'login.html')

def signup(request):
    return render(request , 'signup.html')

def logout(request):
    # logout(request)
    return redirect('login')

def upload_photo(request):

    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")

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
            image=image
        )

        messages.success(request, "Photo uploaded successfully!")
        return redirect("upload")

    photos = Photo.objects.all()
    return render(request, "pics.html", {"photos": photos})

