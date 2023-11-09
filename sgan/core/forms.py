from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from .models import ModelUsuario

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
        



        


     