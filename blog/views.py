from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
  context = {
    'blogs': Post.objects.all()
  }
  return render(request, 'pages/index.html', context)

def contact(request):
  return render(request, 'pages/contact.html')