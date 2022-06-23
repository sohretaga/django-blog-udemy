from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel

# Register your models here.


class CustomUserModelAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
      ('Avatar ', {
        'fields':['avatar']
      }),
    )

admin.site.register(CustomUserModel, CustomUserModelAdmin)