from django import template
from blog.models import Category

register = template.Library()

@register.simple_tag
def categories():
  category = Category.objects.all()
  return category