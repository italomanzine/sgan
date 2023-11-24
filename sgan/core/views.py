from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm, TreinoForm
from .models import Treino


def index(request):
    return render(request, 'index.html', {'titulo_pagina': 'Página Inicial'})

def treinos(request):
    return render(request, 'treinos.html', {'titulo_pagina': 'Treinos'})

def atletas(request):
    return render(request, 'atletas.html', {'titulo_pagina': 'Atletas'})

def dashboard(request):
    return render(request, 'dashboard.html', {'titulo_pagina': 'Dashboard'})

def resultados(request):
    return render(request, 'resultados.html', {'titulo_pagina': 'Resultados'})

def provas(request):
    return render(request, 'provas.html', {'titulo_pagina': 'Provas'})

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

# A view que lida com a criação de treinos
def create_treino(request):
    if not (request.user.is_superuser or request.user.is_staff):
        # Se o usuário não tem permissão, retorna à página de treinos com uma mensagem de erro
        messages.error(request, 'Você não tem permissão para criar treinos.')
        return redirect('treinos')
    
    if request.method == 'POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            # Se o formulário é válido, salva o novo treino e redireciona para a página de treinos
            form.save()
            messages.success(request, 'Treino criado com sucesso!')
            return redirect('treinos')
        else:
            # Se o formulário não é válido, retorna à página com o formulário e mensagens de erro
            return render(request, 'treinos.html', {'form': form})
    else:
        # Se não for uma requisição POST, exibe a página com o formulário de criação de treinos
        form = TreinoForm()
        return render(request, 'create_treino.html', {'form': form})
