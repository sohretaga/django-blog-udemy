from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomAdmin(UserAdmin):
  model = CustomUser
  list_display = ('username', 'email', 'is_superuser')
  fieldsets = UserAdmin.fieldsets + (
    ('Change Avatar', {
      'fields':['avatar']
    }),
  )