from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Photo
# Create your views here.



def  home(request):
    return render(request , 'home.html')

def  basedemo(request):
    return render(request , 'base.html')



def upload_photo(request):

    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")

        Photo.objects.create(
            title=title,
            image=image
        )

        return redirect("upload")

    photos = Photo.objects.all()

    return render(request,"pics.html", {"photos": photos})