from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import atletas, dashboard, deletar_treino, editar_treino, index, resultados, treinos_list, user, create_treino, login_view, provas, presenca, novo_usuario, resultado
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

from .views import provas, create, view, edit, update, delete_prova, create_resultado

urlpatterns = [
    path('index/', login_required(index), name='index'),
    path('user/', login_required(user), name='user'),

    # URL para a view de login
    path('', login_view, name='login'),

    # URLs para logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # URLs para redefinição de senha
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # URLs do Menu Lateral
    path('dashboard/', login_required(dashboard), name='dashboard'),
    path('atletas/', login_required(atletas), name='atletas'),
    path('treinos/', login_required(treinos_list), name='treinos'),
    path('resultados/', login_required(resultados), name='resultados'),
    path('presenca/', login_required(presenca), name='presenca'),    
    path('novo_usuario/', login_required(novo_usuario), name='novo_usuario'),  
    
    

    #URLs para treinos
    path('treinos/create/', login_required(create_treino), name='create_treino'),
    path('treinos/editar/<int:treino_id>/', login_required(editar_treino), name='editar_treino'),
    # path('treinos/responder/<int:treino_id>/', responder_pse, name='responder_pse'),
    path('treinos/deletar/<int:treino_id>/', login_required(deletar_treino), name='deletar_treino'),

    #para provas 
    path('provas/', login_required(provas), name='provas'),
    path('provas/create/', login_required(create), name='create_prova'),
    path('provas/<int:pk>/', login_required(view), name='view_prova'),
    path('provas/<int:pk>/edit/', login_required(edit), name='edit_prova'),
    path('provas/<int:pk>/update/', login_required(update), name='update_prova'),
    path('delete_prova/', login_required(delete_prova), name='delete_prova'),


    
    #para pagina de atleta 
    path('resultado/', login_required(resultado), name='resultado'),
    path('provas/create_resultado/', login_required(create_resultado), name='create_resultado'),

    #PARA PAGINA DE RESULTADO

  


    

   
]