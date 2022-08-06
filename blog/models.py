from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
  title = models.CharField(max_length=50, blank=False, null=False)
  slug = AutoSlugField(populate_from = 'title', unique = True)

  class Meta:
    db_table = 'category'
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  def __str__(self) -> str:
    return self.title


class Post(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField()
  image = models.ImageField(upload_to = 'post_images')
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')
  slug = AutoSlugField(populate_from = 'title', unique = True)
  category = models.ManyToManyField(Category, related_name='category_post')
  created_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'post'
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'