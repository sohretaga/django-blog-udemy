from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

def index(request):
  context = {
    'blogs': Paginator(Post.objects.all().order_by('-created_date'), 2).get_page(request.GET.get('page'))
  }
  return render(request, 'pages/index.html', context)

def contact(request):
  return render(request, 'pages/contact.html')