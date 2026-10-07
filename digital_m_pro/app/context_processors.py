from .models import Location


def site_location(request):
    location = Location.objects.filter(
        is_active=True
    ).first()

    return {
        "site_location": location
    }