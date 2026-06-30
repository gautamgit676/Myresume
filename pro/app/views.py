from django.shortcuts import render

# Create your views here.


def  home(request):
    return render(request , 'home.html')


from django.shortcuts import render, redirect
from .models import Photo

def upload_photo(request):

    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")

        Photo.objects.create(
            title=title,
            image=image
        )

        return redirect("upload")

    photos = Photo.objects.values()

    return render(request,"pics.html", {"photos": photos})