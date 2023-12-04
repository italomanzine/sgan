from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm, DescricaoTreinoForm, TreinoForm
from .models import DescricaoTreino, Treino
from django.db import transaction
from django.views import View
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from .models import Prova, Resultado, ModelUsuario
from .forms import ProvaForm, ResultadoForm

import logging
logger = logging.getLogger(__name__)

# ... no início da sua função de view
logger.info('Mensagem informativa')
logger.warning('Aviso')
logger.error('Erro')


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

def presenca(request):
    return render(request, 'presenca.html', {'titulo_pagina': 'Presença'})

def novo_usuario(request):
    return redirect('/admin/')

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
@login_required
def create_treino(request):
    treino_form = TreinoForm(request.POST or None)
    descricao_treino_form = DescricaoTreinoForm(request.POST or None)

    if request.method == 'POST':
        if not (request.user.is_superuser or request.user.is_staff):
            messages.error(request, 'Você não tem permissão para criar treinos.')
            return redirect('treinos')

        if treino_form.is_valid() and descricao_treino_form.is_valid():
            with transaction.atomic():
                treino = treino_form.save()
                descricao_treino = descricao_treino_form.save(commit=False)
                descricao_treino.treino = treino
                descricao_treino.save()
                messages.success(request, 'Treino criado com sucesso!')
                return redirect('treinos')
        else:
            # Se os formulários não forem válidos, as mensagens de erro serão adicionadas automaticamente
            pass

    # O contexto sempre incluirá os formulários, seja em uma requisição GET ou POST com dados inválidos
    return render(request, 'treinos.html', {
        'treino_form': treino_form,
        'descricao_treino_form': descricao_treino_form
    })

# A view que lida com a visualização de treinos   
@login_required
def treinos_list(request):
    descricao_treinos = DescricaoTreino.objects.select_related('treino', 'modelusuario').all()
    context = {
        'titulo_pagina': 'Treinos',
        'descricao_treinos': descricao_treinos,
        'pode_editar': request.user.has_perm('app.change_treino'),
        'pode_deletar': request.user.has_perm('app.delete_treino'),
        'pode_responder': request.user.has_perm('app.responder_pse'),
    }
    return render(request, 'treinos.html', context)

# A view que lida com a edição de treinos
@permission_required('app.change_treino', raise_exception=True)
def editar_treino(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)
    if request.method == 'POST':
        form = TreinoForm(request.POST, instance=treino)
        if form.is_valid():
            form.save()
            messages.success(request, 'Treino atualizado com sucesso!')
            # Novamente, certifique-se de que 'lista_de_treinos' é o nome correto da URL.
            return redirect('treinos')
    else:
        form = TreinoForm(instance=treino)
    return render(request, 'editar_treino.html', {'form': form})

# A view que lida com a exclusão de treinos
@permission_required('app.delete_treino', raise_exception=True)
def deletar_treino(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)
    treino.delete()
    messages.success(request, 'Treino deletado com sucesso!')
    # Certifique-se de que 'lista_de_treinos' é o nome correto da URL para a lista de treinos.
    return redirect('treinos')

# A view que lida com a resposta ao PSE
# @login_required
# def responder_pse(request, treino_id):
#     # Pegar a instancia do treino
#     treino = get_object_or_404(Treino, id=treino_id)
#     # Pegar a instancia da descrição do treino para o usuário logado e o treino selecionado
#     descricao_treino, created = DescricaoTreino.objects.get_or_create(treino=treino, modelusuario=request.user)

#     # Verifica se o usuário é um atleta
#     if not request.user.has_perm('app.responder_pse'):
#         messages.error(request, 'Você não tem permissão para responder ao PSE.')
#         return redirect('nome_da_url_para_lista_de_treinos')

#     if request.method == 'POST':
#         form = DescricaoTreinoForm(request.POST, instance=descricao_treino)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'PSE e presença respondidos com sucesso!')
#             return redirect('nome_da_url_para_lista_de_treinos')
#         else:
#             messages.error(request, 'Houve um erro ao responder ao PSE.')
#     else:
#         form = DescricaoTreinoForm(instance=descricao_treino)
    
#     # Renderiza a página com o formulário para responder ao PSE
#     return render(request, 'responder_pse.html', {'form': form, 'treino': treino})

#para prova 
def provas(request):
    provas_list = Prova.objects.all()
    modelusuarios_list = ModelUsuario.objects.all()  # Adicione esta linha
    return render(request, 'provas.html', {'provas_list': provas_list, 'modelusuarios_list': modelusuarios_list})

def create(request):
    if request.method == 'POST':
        prova_id = request.POST.get('prova_id')

        # Se prova_id estiver presente, é uma edição
        if prova_id:
            prova = Prova.objects.get(pk=prova_id)
        else:
            prova = Prova()

        # Atualize ou crie os campos da prova
        prova.nome_prova = request.POST.get('nome_prova')
        prova.distancia = request.POST.get('distancia')
        prova.estilo = request.POST.get('estilo')
        prova.naipe = request.POST.get('naipe')
        
        prova.save()
    return redirect('provas')

def view(request):
    provas = Prova.objects.all()  # Substitua Prova pelo nome correto do seu modelo
    return render(request, 'seu_template.html', {'provas': provas})

def edit(request, pk):
    data = {}
    data['prova'] = Prova.objects.get(pk=pk)
    data['form'] = ProvaForm(instance=data['prova'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['prova'] = Prova.objects.get(pk=pk)
    form = ProvaForm(request.POST or None, instance=data['prova'])
    if form.is_valid():
        form.save()
        return redirect('provas')

@require_POST
def delete_prova(request):
    prova_id = request.POST.get('prova_id')
    
    try:
        prova = get_object_or_404(Prova, pk=prova_id)
        prova_nome = prova.nome_prova
        prova.delete()
        messages.success(request, f"A prova '{prova_nome}' foi excluída com sucesso.")
        return redirect('provas')
    except Exception as e:
        messages.error(request, f"Erro ao excluir a prova: {str(e)}")
        return redirect('provas')

#PARA COLOCAR OS DADOS NO BANCO DE DADOS DA TABELA DE RESULTADO 

def resultado(request):
    # Retrieve all Prova objects from the database
    #reultado_list = Resultado.objects.all()
    return render(request, 'provas.html')

def create_resultado(request):
    if request.method == 'POST':
        form = ResultadoForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('provas')  # Altere para a URL correta da página de resultados
            else:
                print("Formulário inválido:", form.errors)
        except Exception as e:
            print("ok", e)
    else:
        form = ResultadoForm()

    provas_list = Prova.objects.all()
    modelusuarios_list = ModelUsuario.objects.all()  # Adicione esta linha
    return render(request, 'provas.html', {'form': form, 'provas_list': provas_list, 'modelusuarios_list': modelusuarios_list})


#para pagina de atleta
def atletas(request):
    modelusuarios_list = ModelUsuario.objects.all()  # Adicione esta linha
    return render(request, 'atletas.html', {'modelusuarios_list': modelusuarios_list})

def mostrar_atletas(request):
    if request.method == 'POST':
        form = ResultadoForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('atletas')  # Altere para a URL correta da página de resultados
            else:
                print("Formulário inválido:", form.errors)
        except Exception as e:
            print("ok", e)
    else:
        form = ResultadoForm()

    modelusuarios_list = ModelUsuario.objects.all()  # Adicione esta linha
    return render(request, 'atletas.html', {'form': form, 'modelusuarios_list': modelusuarios_list})


def detalhes_atleta(request):
    atleta_id = request.GET.get('atleta_id')
    atleta = get_object_or_404(ModelUsuario, pk=atleta_id)

    # Retornando os detalhes do atleta como JSON
    response_data = {
        'email': atleta.email,
        'nome': atleta.get_full_name(),
        'nascimento': str(atleta.data_nascimento),
        'sexo': atleta.get_sexo_display(),
        # Adicione outros campos conforme necessário
    }

    return JsonResponse(response_data)

#PARA A PAGINA DE RESULTADO 
