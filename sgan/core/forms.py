from multiprocessing import AuthenticationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from .models import DescricaoTreino, ModelUsuario, Treino, Prova, Resultado
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from django.utils.dateparse import parse_duration
from datetime import timedelta
from dateutil.parser import parse
from datetime import datetime, timedelta

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
    
class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['descricao']  # Inclua apenas os campos que existem no modelo Treino

class DescricaoTreinoForm(forms.ModelForm):
    class Meta:
        model = DescricaoTreino
        exclude = ['treino']  # Exclui o campo treino do formulário, pois ele será definido na view
        fields = ['treino', 'PSE_treinador', 'data_treino']


# PARA PROVAS  
class ProvaForm(forms.ModelForm):
    class Meta:
        model = Prova
        #fields = ['nome_prova', 'estilo']
        fields = ['nome_prova', 'distancia', 'estilo', 'naipe']

    def save(self, commit=True):
        # Verifique se os dados estão sendo manipulados corretamente
        instancia_prova = super().save(commit=False)
        instancia_prova.distancia = self.cleaned_data['distancia']
        instancia_prova.naipe = self.cleaned_data['naipe']
        
        if commit:
            instancia_prova.save()
        return instancia_prova

#PARA RESULTADOS
class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ['modelusuario', 'prova', 'tempo', 'classificacao', 'data_prova']

    def clean_tempo(self):
        tempo = self.cleaned_data['tempo']

        try:
            # Verifique se já é um objeto timedelta
            if isinstance(tempo, timedelta):
                return tempo

            # Converta a string de tempo em um objeto timedelta
            tempo_timedelta = timedelta(seconds=float(tempo))
        except ValueError:
            raise forms.ValidationError("Formato de tempo inválido. Use HH:MM:SS.ssssss")

        return tempo_timedelta

    def save(self, commit=True):
        instancia_resultado = super().save(commit=False)
        instancia_resultado.tempo = self.cleaned_data['tempo']
        instancia_resultado.classificacao = self.cleaned_data['classificacao']
        
        if commit:
            instancia_resultado.save()
        return instancia_resultado
    

#PARA PAGINA DE ATLETAS
