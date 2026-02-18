# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.product_preview, name='product_preview'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/add/', views.add_product, name='add_product'),
    path('admin-dashboard/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('admin-dashboard/delete/<int:pk>/', views.delete_product, name='delete_product'),
]