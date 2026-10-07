from django.urls import path
from app.views import *



urlpatterns = [
    # path('', home , name='home'),
     # Main pages
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('membership/', membership, name='membership'),
    path('personal-training/', personal_training, name='personal-training'),
    path('gym-fees-ahmedabad/', pricing, name='gym-fees-ahmedabad'),
    path('weight-loss/', weightloss, name='weight-loss'),
    path('pricing/', pricing, name='pricing'),
    path("robots.txt", robots_txt, name="robots_txt"),

    # Locations
    path('locations/', location, name='locations'),

    # Blog
    path('blog/', blog, name='blog'),
    # path('location/ahmedabad/', locat/ion , name='location_ahmedabad'),
]
