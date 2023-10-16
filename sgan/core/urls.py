from django.urls import path
from .views import index, user

urlpatterns = [
    path('', index),
    path('user', user),
]
