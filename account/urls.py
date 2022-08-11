from django.urls import path
from .views import userLogout, changePassword

urlpatterns = [
  path('logout/', userLogout, name='logout'),
  path('change-password/', changePassword, name='change-password'),
]