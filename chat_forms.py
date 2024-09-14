# chat/forms.py
from django import forms
from django.contrib.auth.models import User

from .models import Message


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
