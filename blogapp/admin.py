from django.contrib import admin
from blogapp.models import CategoryModule, ArticleModel, CommentsModel, ContactModel

# Register your models here.

admin.site.register(CategoryModule)
admin.site.register(ArticleModel)
admin.site.register(CommentsModel)
admin.site.register(ContactModel)