from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from account.forms import UpdateAccountForm, UserCreateForm
from django.contrib import messages

# Create your views here.

@login_required(login_url='/')
def userLogout(request):
  logout(request)
  messages.success(request, 'Logout successfuly!')
  return redirect('index')

def changePassword(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      messages.success(request, 'Password changed!')
      return redirect('myblogs')
  else:
    form = PasswordChangeForm(request.user)
  context = {
    'form': form
  }
  return render(request, 'change-password.html', context)

@login_required(login_url='/')
def updateAccount(request):
  if request.method == 'POST':
    form = UpdateAccountForm(request.POST, request.FILES, instance = request.user)
    form.save()
    messages.success(request, 'Account updated!')
  else:
    form = UpdateAccountForm(instance = request.user)
  context = {
    'form': form
  }
  return render(request, 'update-account.html', context)


def signUp(request):
  if request.method == 'POST':
    form = UserCreateForm(request.POST)
    if form.is_valid():
      form.save()
      login(request, user=authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1']))
      messages.success(request, 'Register successfly!')
      return redirect('index')
      
  else:
    form = UserCreateForm()
  context = {
    'form': form
  }

  return render(request, 'signup.html', context)