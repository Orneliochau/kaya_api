from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from account.models import CustomUser

class UserSignupForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'Nome Completo:'}) )
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone_number']