from django.urls import path
from .views import userLogout, changePassword, updateAccount, signUp

urlpatterns = [
  path('logout/', userLogout, name='logout'),
  path('change-password/', changePassword, name='change-password'),
  path('update-account/', updateAccount, name='update-account'),
  path('sign-up/', signUp, name='sign-up'),
]