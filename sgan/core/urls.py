from django.urls import path
from .views import atletas, dashboard, index, resultados, treinos, user, create_treino, login_view, provas, presenca, novo_usuario, resultado
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

from .views import provas, create, view, edit, update, delete_prova, create_resultado

urlpatterns = [
    path('', index, name='index'),
    path('user/', user),

    # URL para a view de login
    path('login/', login_view, name='login'),

    # URLs para logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # URLs para redefinição de senha
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # URLs do Menu Lateral
    path('dashboard/', dashboard, name='dashboard'),
    path('atletas/', atletas, name='atletas'),
    path('treinos/', treinos, name='treinos'),
    path('resultados/', resultados, name='resultados'),
    path('presenca/', presenca, name='presenca'),    
    path('novo_usuario/', novo_usuario, name='novo_usuario'),  
    path('novo_usuario/', novo_usuario, name='novo_usuario'),  
    
    

    #URLs para treinos
    path('treinos/create/', create_treino, name='create_treino'),

    #para provas 
    path('provas/', provas, name='provas'),
    path('provas/create/', create, name='create_prova'),
    path('provas/<int:pk>/', view, name='view_prova'),
    path('provas/<int:pk>/edit/', edit, name='edit_prova'),
    path('provas/<int:pk>/update/', update, name='update_prova'),
    path('delete_prova/', delete_prova, name='delete_prova'),


    
    #para pagina de atleta 
    path('resultado/', resultado, name='resultado'),
    path('provas/create_resultado/', create_resultado, name='create_resultado'),

    #PARA PAGINA DE RESULTADO

  


    

   
]