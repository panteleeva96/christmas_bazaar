from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import SignUpForm


def user_profile(request):
    pass


def signup_user(request):
    if request.method == 'GET':
        context = {
            'user_form': SignUpForm()
        }
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

        context = {
            'user_form': form
        }
        return render(request, 'accounts/signup.html', context)


def signout_user(request):
    logout(request)
    return redirect('index')