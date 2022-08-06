from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug')

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'category', 'author', 'created_date')