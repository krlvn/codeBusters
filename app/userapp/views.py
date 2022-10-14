from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from userapp.forms import MyUserRegisterForm
from django.contrib import auth
from userapp.forms import MyUserLoginForm


def login(request):
    login_form = MyUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return redirect('/')
    content = {'login_form': login_form}
    return render(request, 'userapp/login.html', content)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        register_form = MyUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        register_form = MyUserRegisterForm()
    content = {'register_form': register_form}
    return render(request, 'userapp/register.html', content)
