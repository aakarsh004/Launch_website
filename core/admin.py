# core/admin.py

from django.contrib import admin
from .models import Product, Subscriber

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status', 'image_preview']
    fields = ['name', 'description', 'image', 'image_url', 'category', 'status', 'launch_date']
    readonly_fields = ['created_at']

    def image_preview(self, obj):
        return obj.image_preview()  # Uses model method
    image_preview.short_description = 'Preview'

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at']