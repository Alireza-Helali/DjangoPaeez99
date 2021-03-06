from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from .forms import LoginForm
from .forms import CustomUserCreationForm


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            # logout(request)
            return redirect('/')
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                return redirect('login')


class SignUp(View):
    def get(self, request):
        form = CustomUserCreationForm()
        context = {
            'form': form
        }

        return render(request, 'signup.html', context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
# @permission_required('user_profile.can_dance',  raise_exception=True)
def gher_umdan(request):
    if request.user.has_perm('user_profile.can_dance'):
        return HttpResponse('Baba Karam!')
    return HttpResponse('raghs harameh!')
