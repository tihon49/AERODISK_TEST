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
