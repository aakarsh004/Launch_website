# core/forms.py
from django import forms
from .models import Subscriber, Product

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email...',
                'required': True
            })
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'status', 'launch_date']
        widgets = {
            'launch_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }