from multiprocessing import AuthenticationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from .models import ModelUsuario
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

class ModelUsuarioCreateForm(UserCreationForm):

    class Meta:
        model=ModelUsuario
        fields=('first_name', 'last_name','fone','data_nascimento','sexo', 'cpf','endereco','curso', 'matricula', 'socio')
        labels={'username': 'Username/E-mail'}

    def save(self, commit=True):
        user=super().save(commit=False) #commit=False faz salvar na variavel, mas não grava no BD
        user.set_password(self.cleaned_data["password1"]) #seta a senha
        user.email=self.cleaned_data['username'] #seta o username no campo de email
        


        if commit:
            user.save()
            
        return user

class ModelUsuarioChangeForm(UserChangeForm):
    class Meta:
        model=ModelUsuario
        fields=('first_name', 'last_name', 'fone','data_nascimento','sexo', 'cpf','endereco','curso', 'matricula', 'socio')

User = get_user_model()
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254)

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': True})

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)

    def clean_username(self):
        username = self.cleaned_data['username']
        return User.objects.normalize_email(username)