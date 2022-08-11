from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

@login_required(login_url='/')
def userLogout(request):
  logout(request)
  return redirect('index')

def changePassword(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      return redirect('myblogs')
  else:
    form = PasswordChangeForm(request.user)
  context = {
    'form': form
  }
  return render(request, 'change-password.html', context)