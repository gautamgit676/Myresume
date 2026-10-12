from .models import Location


# when we need to same data in multiple views then we use context processoor 

def site_location(request):
    location = Location.objects.filter(
        is_active=True).first()

    return {"site_location": location}

