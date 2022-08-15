from django.urls import path
from . import views
from django.views.generic import TemplateView, RedirectView

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
  path('delete-commet/<int:id>/', views.deleteComment, name='delete-comment'),
  path('about/', TemplateView.as_view(template_name = 'pages/about.html'), name='about'),
  path('redirect/', RedirectView.as_view(url='/about')),
  path('email-sended/', TemplateView.as_view(template_name = 'pages/s-mail.html'), name='email-sended'),
]