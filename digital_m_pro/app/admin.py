from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Location, SEOPage


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'state',
        'city',
        'area',
        'slug',
        'is_active',
    )

    list_filter = (
        'state',
        'city',
        'is_active',
    )

    search_fields = (
        'state',
        'city',
        'area',
        'slug',
    )

    prepopulated_fields = {
        'slug': ('area',),
    }
    

admin.site.register(SEOPage)