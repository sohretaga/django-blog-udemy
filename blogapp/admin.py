from django.contrib import admin
from blogapp.models import CategoryModule, ArticleModel, CommentsModel

# Register your models here.

admin.site.register(CategoryModule)
admin.site.register(ArticleModel)
admin.site.register(CommentsModel)