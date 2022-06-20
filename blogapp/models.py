from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

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
  content = RichTextField()
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