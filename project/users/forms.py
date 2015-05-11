from django.forms import ModelForm
from users.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['about']
