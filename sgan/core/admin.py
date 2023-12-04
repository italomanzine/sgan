from django.contrib import admin

# Register your models here.
# importts necessarios para a administração do nosso usuario 
from django.contrib.auth.admin import UserAdmin
from .forms import ModelUsuarioCreateForm, ModelUsuarioChangeForm
from .models import ModelUsuario

@admin.register(ModelUsuario)  
class ModelUsuarioAdmin(UserAdmin):
    add_form=ModelUsuarioCreateForm  #o CreateForm passara a ser o formulario para adicionar novos usuarios 
    form= ModelUsuarioChangeForm #o ChargeForm servira para alteração dos usuarios 
    model=ModelUsuario
    list_display=('first_name', 'last_name', 'email', 'fone', 'is_staff','data_nascimento','sexo', 'cpf','endereco','curso', 'matricula', 'socio')

    #quais dados apresentarao acessar a area administrativa? veja:
    fieldsets=(
        (None, {'fields':('email', 'password')}),
        ('Informações pessoais', {'fields':('first_name', 'last_name', 'fone', 'data_nascimento','sexo', 'cpf','endereco','curso', 'matricula', 'socio')} ),
        ('permissoes',{'fields':('is_active', 'is_staff')}),
    )




    