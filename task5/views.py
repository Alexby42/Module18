from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
info = {}
users = ['ab', 'cd', 'ef']
def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username in users:
            info['error'] = 'Пользователь уже существует'
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Repeat_password: {repeat_password}')
        print(f'Age: {age}')
        print(info)
        return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'registration_page.html', context=info)

def sign_up_by_django(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #form.save()
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')
            repeat_password = form.cleaned_data('repeat_password')
            age = form.cleaned_data('age')
            registration = form.cleaned_data('registration')
            user = authenticate(username=username, password=password, repeat_password=repeat_password, age=age)
            login(request, user)
            return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = ContactForm()
    return render(request, 'registration_page.html', {'form': form})
