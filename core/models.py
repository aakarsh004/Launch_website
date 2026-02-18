# core/models.py
from django.db import models
from django.utils.safestring import mark_safe

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('bags', 'Crochet Bags'),
        ('keychains', 'Crochet Keychains'),
        ('flowers', 'Crochet Flowers'),
        ('home', 'Home Decor'),
        ('custom', 'Custom Orders'),
    ]

    STATUS_CHOICES = [
        ('coming_soon', 'Coming Soon'),
        ('featured', 'Featured'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Made optional
    image_url = models.URLField(max_length=500, blank=True, null=True)       # NEW: External URL field
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='coming_soon')
    launch_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def display_image_url(self):
        """
        Returns the image URL to display in templates.
        Priority: image_url > image > placeholder
        """
        if self.image_url:
            return self.image_url
        elif self.image:
            return self.image.url
        else:
            return "https://via.placeholder.com/300x200?text=No+Image"

    def image_preview(self):
        """For Django Admin: shows a thumbnail preview."""
        if self.display_image_url:
            return mark_safe(f'<img src="{self.display_image_url}" width="50" style="border-radius: 4px;" />')
        return "No image"
    image_preview.short_description = 'Preview'


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email