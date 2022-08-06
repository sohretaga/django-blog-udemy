from django.db import models
from autoslug import AutoSlugField
from account.models import CustomUser
from ckeditor.fields import RichTextField
from config.abstracts import DateAbstractModel

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


class Post(DateAbstractModel):
  title = models.CharField(max_length=50)
  content = RichTextField()
  image = models.ImageField(upload_to = 'post_images')
  author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_post')
  slug = AutoSlugField(populate_from = 'title', unique = True)
  category = models.ManyToManyField(Category, related_name='category_post')

  class Meta:
    db_table = 'post'
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def __str__(self) -> str:
    return self.title


class Comment(DateAbstractModel):
  author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment')
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  comment = models.TextField()

  class Meta:
    db_table = 'comments'
    verbose_name = 'Comment'
    verbose_name_plural = 'Comments'

  def __str__(self) -> str:
    return self.author.username


class Contact(models.Model):
  email = models.EmailField(max_length=250)
  full_name = models.CharField(max_length=150)
  message = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'contact'
    verbose_name = 'Contact'
    verbose_name_plural = 'Contacts'
  
  def __str__(self) -> str:
    return self.full_name

