from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator

# Create your views here.

def index(request):
  context = {
    'blogs': Paginator(Post.objects.all().order_by('-created_date'), 2).get_page(request.GET.get('page'))
  }
  return render(request, 'pages/index.html', context)

def category(request, slug):
  context = {
    'blogs': Paginator(get_object_or_404(Category, slug=slug).category_post.order_by('-created_date'), 2).get_page(request.GET.get('page')),
    'category_name': Category.objects.get(slug=slug).title
  }
  return render(request, 'pages/categories.html', context)

def contact(request):
  return render(request, 'pages/contact.html')


def myblogs(request):
  context = {
    'blogs': Paginator(request.user.author_post.order_by('-created_date'), 2).get_page(request.GET.get('page'))
  }
  return render(request, 'pages/myblogs.html', context)