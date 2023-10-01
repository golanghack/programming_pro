from django.contrib import admin
from app.models import Product, Lesson

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'owner', 'permiss']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name_of_lesson', 'video', 'duration', 'visited']
    list_filter = ['duration', 'visited']
    search_fields = ['name_of_lesson', 'duration']
    