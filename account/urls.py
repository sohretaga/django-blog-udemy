from django.urls import path
from .views import userLogout, changePassword, updateAccount, signUp
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('logout/', userLogout, name='logout'),
  path('change-password/', changePassword, name='change-password'),
  path('update-account/', updateAccount, name='update-account'),
  path('sign-up/', signUp, name='sign-up'),
  path('login/', auth_views.LoginView.as_view(
    template_name = 'signin.html'
    ), name='sign-in'),
  
]