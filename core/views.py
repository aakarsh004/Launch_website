# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Subscriber
from .forms import SubscriberForm, ProductForm

def home(request):
    form = SubscriberForm()
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! We'll notify you when we launch ❤️")
            return redirect('core:home')
    products = Product.objects.filter(status='featured')[:6]  # Show featured on homepage
    context = {
        'form': form,
        'products': products,
        'launch_date': "2026-02-19T00:00:00"  # Hardcoded for demo — or pull from DB setting
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def product_preview(request):
    products = Product.objects.all().order_by('-created_at')
    categories = Product.CATEGORY_CHOICES
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'core/products.html', context)

def subscribe(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You’re on the list! 💌")
    return redirect('core:home')

# ===== ADMIN DASHBOARD =====
def admin_dashboard(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'core/admin_dashboard.html', {'products': products})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('core:admin_dashboard')
    else:
        form = ProductForm()
    return render(request, 'core/add_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated!")
            return redirect('core:admin_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'core/edit_product.html', {'form': form, 'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted.")
        return redirect('core:admin_dashboard')
    return render(request, 'core/confirm_delete.html', {'product': product})