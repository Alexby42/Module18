from django import forms
#from django.contrib.auth.forms import ContactForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from task5.views import users


# Create your views here.

class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label='Ваше имя')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Ваш пароль')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите пароль')
    age = forms.IntegerField(max_length=3, label='Ваш возраст')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        age = cleaned_data.get('age')
        if username in users:
            self.add_error('username', 'Пользователь уже существует')
        if password != repeat_password:
            self.add_error('repeat_password', 'Пароли не совпадают')
        if age is not None and age < 18:
            self.add_error('age', 'Вы должны быть старше 18')
