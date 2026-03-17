from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register
class AdminProducts(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'category', 'updated', 'created']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}