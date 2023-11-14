from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def user(request):
    return render(request, 'user.html')

def login_view(request):  # Esta é a função renomeada
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)  # Use o nome renomeado aqui
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')  # Substitua 'index' pela URL que você deseja redirecionar após o cadastro
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})