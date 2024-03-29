from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug')

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'created_date')
  search_fields = ('title',)

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('author', 'post', 'created_date')
  search_fields = ('author__username',)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'email', 'created_date')
  list_filter = ('created_date',)
  search_fields = ('email',)