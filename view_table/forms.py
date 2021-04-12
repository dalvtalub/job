from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm


class AuthForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
