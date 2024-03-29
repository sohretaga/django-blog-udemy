from tkinter.tix import Tree
from django.db import models

class DateAbstractModel(models.Model):
  created_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True