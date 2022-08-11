from django.contrib.auth.forms import UserChangeForm
from account.models import CustomUser

class UpdateAccountForm(UserChangeForm):
  password = None
  class Meta:
    model = CustomUser
    fields = ('first_name', 'last_name', 'email', 'avatar')