from django import forms
from .models import Contact, Post, Comment

class ContactForm(forms.ModelForm):
  #         forms.Form
  # email = forms.EmailField(label='Email')
  # full_name = forms.CharField(label='Full Name', max_length=100)
  # message = forms.CharField(label='Message', widget=forms.Textarea)

  class Meta:
    model = Contact
    fields = ('full_name', 'email', 'message')


# (attrs={
#     'class':'form-control'
#   })


class BlogForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ('author', 'slug')


class UpdateBlogForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ('author', 'slug')

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('comment',)