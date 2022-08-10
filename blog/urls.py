from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('contact/', views.contact, name='contact'),
  path('category/<slug:slug>/', views.category, name='category'),
  path('myblogs/', views.myblogs, name='myblogs'),
  path('search/', views.search, name='search'),
  path('detail/<slug:slug>/', views.detail, name='detail'),
  path('add-blog/', views.addBlog, name='add-blog'),
  path('update-blog/<slug:slug>/', views.updateBlog, name='update-blog'),
  path('delete/<slug:slug>', views.deleteBlog, name='delete-blog'),
]