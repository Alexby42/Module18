from django import forms
#from django.contrib.auth.forms import ContactForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from task5.views import users


# Create your views here.

class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label='Ваше имя')
    password = forms.CharField(min_length=8, label='Ваш пароль')
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль')
    age = forms.CharField(max_length=3, label='Ваш возраст')
    #registration = forms.BooleanField(required=False, label='Зарегистрироваться')

    def clean(self):
        global username, age
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        if username in users:
            raise forms.ValidationError('Пользователь уже существует')
        if password != repeat_password:
            raise forms.ValidationError('Пароли не совпадают!')
        if int(age) < 18:
            raise forms.ValidationError('Вы должны быть старше 18')
        return
