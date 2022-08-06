from django.db import models
from autoslug import AutoSlugField

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