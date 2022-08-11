import re
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ContactForm, BlogForm, UpdateBlogForm, CommentForm
from django.contrib import messages

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
  if request.method == 'POST':
    add_comment_form = CommentForm(data=request.POST)
    if add_comment_form.is_valid():
      newCommet = add_comment_form.save(commit=False)
      newCommet.author = request.user
      newCommet.post = get_object_or_404(Post, slug=slug)
      newCommet.save()
  add_comment_form = CommentForm()
  context={
    'blog': get_object_or_404(Post, slug=slug),
    'comments': get_object_or_404(Post, slug=slug).comments.all(),
    'add_comment_form': add_comment_form
  }
  return render(request, 'pages/detail.html', context)

@login_required(login_url='/')
def addBlog(request):
  form = BlogForm(request.POST or None, files=request.FILES or None)
  if form.is_valid():
    newBlog = form.save(commit=False)
    newBlog.author = request.user
    newBlog.save()
    form.save_m2m()
    messages.success(request, 'Blog posted!')
    return redirect('detail', slug=newBlog.slug)
  context = {
    'form': form
  }
  return render(request, 'pages/add-blog.html', context)

@login_required(login_url='/')
def updateBlog(request, slug):
  blog = get_object_or_404(Post, slug=slug, author = request.user)
  form = UpdateBlogForm(request.POST or None, request.FILES or None, instance=blog)
  if form.is_valid():
    form.save()
    messages.success(request, 'Blog updated!')
    return redirect('detail', slug=blog.slug)
  context = {
    'form': form
  }
  return render(request, 'pages/update-blog.html', context)


def deleteBlog(request, slug):
  get_object_or_404(Post, slug=slug, author=request.user).delete()
  messages.success(request, 'Blog deleted!')
  return redirect('myblogs')

@login_required(login_url='/')
def deleteComment(request, id):
  comment = get_object_or_404(Comment, id=id)
  if comment.author == request.user or comment.post.author == request.user:
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect('detail', slug=comment.post.slug)
  return redirect('index')