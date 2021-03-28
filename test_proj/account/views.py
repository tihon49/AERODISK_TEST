from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateUserForm


def registration_view(request):
    """страница регистрации аккаунта"""

    template = 'account/registration.html'
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Создан аккаунт пользователя ' + user)

            return redirect('login')
        else:
            for error in form.errors:
                print(error, ':', form.errors[error])
                if 'A user with that username already exists.' in form.errors[error].as_text():
                    messages.success(request, 'Это имя уже занято')
                    break
                elif 'This password is too common.' in form.errors[error].as_text():
                    messages.success(request, 'Слишком простой пароль. Пароль должен состоять из букв, цифр и быть не короче 8-ми символов')
                    break
                elif 'The two password fields didn' in form.errors[error].as_text():
                    messages.success(request, 'Пароли не совпадают')
                

    context = {'form': form}
    return render(request, template, context)


def login_view(request):
    """страница авторизации"""

    template = 'account/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.info(request, 'Логин или пароль не корректны...')

    return render(request, template)


def logout_view(request):
    logout(request)
    return redirect('login')
