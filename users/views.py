from django.contrib.messages import error, success
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('tasks:tasks'))
    context = {
        'title': 'Register',
        'linked_page': 'Login',
        'linked_page_url': reverse('users:login'),
        'show_labels': True,
    }
    form = RegisterForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        success(request, 'Registration completed.')
        return redirect(reverse('users:login'))
    context['form'] = form  # type: ignore
    context['action'] = reverse('users:register')
    return render(request, 'users/pages/users.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('tasks:tasks'))
    context = {
        'title': 'Login',
        'linked_page': 'Register',
        'linked_page_url': reverse('users:register'),
        'show_labels': True,
    }
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        credentials = {
            'username': form.cleaned_data.get('username'),
            'password': form.cleaned_data.get('password')
        }
        authenticated_user = authenticate(**credentials)
        if not authenticated_user:
            error(request, 'Invalid credentials.')
            return redirect(reverse('users:login'))
        auth_login(request, authenticated_user)
        success(request, f'Login completed.')
        return redirect(reverse('tasks:tasks'))
    context['form'] = form  # type: ignore
    context['action'] = reverse('users:login')
    return render(request, 'users/pages/users.html', context)


@login_required(login_url='users:login')
def logout(request):
    redirect_url = redirect(reverse('tasks:tasks'))
    if not request.POST or request.POST.get('username') != request.user.username:
        error(request, 'An error occurred while logging out.')
        return redirect_url
    auth_logout(request)
    success(request, f'Logout completed.')
    return redirect_url
