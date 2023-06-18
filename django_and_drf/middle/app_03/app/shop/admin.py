from django.contrib import admin
from parler.admin import TraslatableAdmin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(TraslatableAdmin):
    list_display = ['name', 'slug']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(TraslatableAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
