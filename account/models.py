from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
  avatar = models.ImageField(upload_to = 'avatars', blank = True, null=True)

  class Meta:
    db_table = 'user'
    verbose_name = 'User'
    verbose_name_plural = 'Users'

  def __str__(self) -> str:
    return self.username