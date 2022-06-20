from tabnanny import verbose
from django.db import models
from autoslug import AutoSlugField

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