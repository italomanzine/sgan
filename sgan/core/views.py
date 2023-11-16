from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm


def index(request):
    return render(request, 'index.html')

def treinos(request):
    return render(request, 'treinos.html')

def atletas(request):
    return render(request, 'atletas.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def resultados(request):
    return render(request, 'resultados.html')

# def login(request):
#     return render(request, 'login.html')

def user(request):
    return render(request, 'user.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

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