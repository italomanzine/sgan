from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import ModelUsuario


def index(request):
    return render(request, 'index.html')


def user(request):
    return render(request, 'user.html')


"""
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
"""


#parte certa para um dashboard so 
def dashboard(request):
    #return render(request, 'dashboard.html')
    if request.user.is_staff:
        # Se o usuário é um staff, renderize o dashboard de staff
        return render(request, 'dashboard_staff.html')
    else:
        # Se o usuário não é staff, renderize o dashboard padrão
        return render(request, 'dashboard_user.html')
