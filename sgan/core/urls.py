from django.urls import path
from .views import index, user, dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', index, name='index'),
    path('user', user, name='user'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
   

]
