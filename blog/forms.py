from django import forms
from .models import Contact

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