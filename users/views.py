
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})