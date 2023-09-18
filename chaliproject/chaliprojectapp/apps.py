from django.apps import AppConfig
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email']


class ChaliprojectappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chaliprojectapp'



