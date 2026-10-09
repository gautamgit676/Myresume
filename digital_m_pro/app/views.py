from django.shortcuts import render
from django.shortcuts import render
from app.models import *

from django.shortcuts import render, redirect
from django.http import HttpResponse
# # Create your views here.
def robots_txt(request):
    content = """User-agent: *
Disallow: /admin/

Sitemap: https://gautamsinh.duckdns.org/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")

def get_seo(page_path):
    return SEOPage.objects.filter(
        url_path=page_path,
        is_active=True
    ).first()


def get_location():
    return Location.objects.filter(
        is_active=True
    ).first()
    
    

def home(request):
    seo = get_seo("/")
    location = get_location()
    return render(request, 'home.html', {"seo": seo, "location": location})

def about(request):
    seo = get_seo("/about/")
    location = get_location()
    return render(request,'About.html', {"seo": seo, "location": location})

# def contact(request):
#     seo = get_seo("/contact/")
#     location = get_location()
#     print(seo.meta_title,'-=-=-=-=-')
#     return render(request,'Contact.html', {"seo": seo, "location": location})

def contact_success(request):
    return render(request, "contact_success.html")

def contact(request):
    seo = get_seo("/contact/")
    location = get_location()
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Save/send the lead here

        return redirect("contact-success")

    return render(request, "Contact.html", {"seo": seo, "location": location})


def blog(request):
    seo = get_seo("/blog/")
    location = get_location()
    return render(request , 'Blog.html', {"seo": seo, "location": location})

def location(request):
    seo = get_seo("/locations/")
    location = get_location()
    print(seo.meta_title,'-=-=-=-=-')
    return render(request,'Location.html', {"seo": seo, "location": location})


def membership(request):
    seo = get_seo("/membership/")
    location = get_location()
    return render(request,'Membership.html', {"seo": seo, "location": location})


def personal_training(request):
    seo = get_seo("/personal-training/")
    location = get_location()
    return render(request,'PersonalTraining.html', {"seo": seo, "location": location})

def pricing(request):
    seo = get_seo("/gym-fees-ahmedabad/")
    location = get_location()
    return render(request,'Pricing.html', {"seo": seo, "location": location})


def weightloss(request):
    seo = get_seo("/weight-loss/")
    location = get_location()
    return render(request,'WeightLoss.html', {"seo": seo, "location": location})




