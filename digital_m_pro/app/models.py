from django.db import models

# Create your models here.
from django.db import models


class Location(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100, blank=True)

    slug = models.SlugField(max_length=150, unique=True)

    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True)

    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)

    description = models.TextField()

    seo_title = models.CharField(max_length=60, blank=True)
    seo_description = models.CharField(max_length=160, blank=True)

    is_active = models.BooleanField(default=True)
    latitude = models.DecimalField(
    max_digits=9,
    decimal_places=6,
    null=True,
    blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    website_url = models.URLField(
        blank=True
    )

    facebook_url = models.URLField(
        blank=True
    )

    instagram_url = models.URLField(
        blank=True
    )

    linkedin_url = models.URLField(
        blank=True
    )

    price_range = models.CharField(
        max_length=20,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.area:
            return f"{self.area}, {self.city}"
        return self.city
    


class SEOPage(models.Model):
    page_name = models.CharField(max_length=100, unique=True)

    url_path = models.CharField(
        max_length=200,
        unique=True
    )

    meta_title = models.CharField(
        max_length=60
    )

    meta_description = models.CharField(
        max_length=160
    )

    canonical_url = models.URLField(
        blank=True
    )

    robots = models.CharField(
        max_length=100,
        default="index, follow"
    )

    is_active = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.page_name
    




from django.db import models
from django.urls import reverse


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("dumbbells", "Dumbbells"),
        ("bands", "Resistance Bands"),
        ("clothing", "Gym Clothing"),
        ("yoga", "Yoga Mats"),
    ]

    AVAILABILITY_CHOICES = [
        ("in_stock", "In stock"),
        ("out_of_stock", "Out of stock"),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
    )

    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Filename relative to app/static/app/images/products/
    image_filename = models.CharField(max_length=255)

    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default="in_stock",
    )

    seo_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="products/", blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_image_path(self):
        return f"app/images/products/{self.image_filename}"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
