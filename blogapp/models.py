from distutils.command.upload import upload
from email.mime import image
from enum import unique
import imp
from operator import imod
from re import U
from tabnanny import verbose
from unicodedata import category
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.

class CategoryModule(models.Model):
  name = models.CharField(max_length=30, blank=False, null=False)
  slug = AutoSlugField(populate_from = 'name', unique=True)

  class Meta:
    db_table = 'category'
    verbose_name_plural = 'Kateqoriyalar'
    verbose_name = 'Kateqori'
  
  def __str__(self) -> str:
    return self.name


class ArticleModel(models.Model):
  image = models.ImageField(upload_to='article_images')
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  edited_date = models.DateTimeField(auto_now=True)
  slug = AutoSlugField(populate_from='title', unique=True)
  category = models.ManyToManyField(CategoryModule, related_name='article')
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

  class Meta:
    db_table = 'article'
    verbose_name_plural = 'Məqalələr'
    verbose_name = 'Məqalə'
  
  def __str__(self) -> str:
    return self.title