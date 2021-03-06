from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from .abstracts import DateAbstractModel

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


class ArticleModel(DateAbstractModel):
  image = models.ImageField(upload_to='article_images')
  title = models.CharField(max_length=100)
  content = RichTextField()
  slug = AutoSlugField(populate_from='title', unique=True)
  category = models.ManyToManyField(CategoryModule, related_name='article')
  author = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='articles')

  class Meta:
    db_table = 'article'
    verbose_name_plural = 'Məqalələr'
    verbose_name = 'Məqalə'
  
  def __str__(self) -> str:
    return self.title


class CommentsModel(DateAbstractModel):
  commenter = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
  article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, related_name='comments')
  comment = models.TextField()

  class Meta:
    db_table = 'comment'
    verbose_name = 'Rəy'
    verbose_name_plural = 'Rəylər'

  def __str__(self) -> str:
    return self.commenter.username
  

class ContactModel(models.Model):
  full_name = models.CharField(max_length=100)
  email = models.EmailField(max_length=250)
  message = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'contact'
    verbose_name = 'Əlaqə'
    verbose_name_plural = 'Əlaqə'
    
  def __str__(self) -> str:
    return self.full_name
