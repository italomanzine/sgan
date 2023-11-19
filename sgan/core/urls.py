from django.urls import path
from .views import atletas, dashboard, index, resultados, treinos, user, login_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

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
]
