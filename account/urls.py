from django.urls import path
from .views import userLogout, changePassword, updateAccount

urlpatterns = [
  path('logout/', userLogout, name='logout'),
  path('change-password/', changePassword, name='change-password'),
  path('update-account/', updateAccount, name='update-account'),
]