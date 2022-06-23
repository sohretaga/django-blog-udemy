from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserModel(AbstractUser):
  avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

  class Meta:
    db_table = 'user'
    verbose_name = 'Istifadəçi'
    verbose_name_plural = 'Istifadəçilər'

    def __str__(self) -> str:
      return self.username