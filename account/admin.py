from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel

# Register your models here.

@admin.register(CustomUserModel)
class CustomUserModelAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
      ('Avatar ', {
        'fields':['avatar']
      }),
    )
