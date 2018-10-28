from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    account_type = forms.ModelChoiceField(queryset = AccountType.objects.all(), required=False)

    class Meta:
        model = User
        fields = ('username', 'account_type','first_name', 'last_name', 'email', 'password1', 'password2', )