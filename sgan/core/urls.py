from django.urls import path
from .views import index, user, login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('user/', user),

    # URL para a view de login
    path('login/', login_view, name='login'),

    # URLs para redefinição de senha
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
