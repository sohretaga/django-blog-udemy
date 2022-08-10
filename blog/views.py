from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Contact
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ContactForm

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
  # form = ContactForm(data={
  #   'full_name':'test'
  # })
  form = ContactForm(request.POST or None)
  if request.method == 'POST' and form.is_valid():
    # save method for forms.Form
    # Contact.objects.create(
    #   email = form.cleaned_data['email'],
    #   full_name = form.cleaned_data['full_name'],
    #   message = form.cleaned_data['message']
    # ).save()

    # save method for forms.ModelForm
    form.save()
    return redirect('index')
  else:
    print('no valid')
  context = {
    'form': form
  }
  return render(request, 'pages/contact.html', context)

@login_required(login_url='/')
def myblogs(request):
  context = {
    'blogs': Paginator(request.user.author_post.order_by('-created_date'), 20).get_page(request.GET.get('page'))
  }
  return render(request, 'pages/myblogs.html', context)


def search(request):
  if request.GET.get('key'):
    context = {
      'blogs': Paginator(Post.objects.filter(Q(title__icontains=request.GET.get('key')) | Q(content__icontains=request.GET.get('key'))).distinct(), 2).get_page(request.GET.get('page')),
      'key': request.GET.get('key')
    }
  return render(request, 'pages/search.html', context)

def detail(request, slug):
  context={
    'blog': get_object_or_404(Post, slug=slug),
    'comments': get_object_or_404(Post, slug=slug).comments.all()
  }
  return render(request, 'pages/detail.html', context)