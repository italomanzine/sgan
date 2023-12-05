from django.contrib import admin

# Register your models here.
# importts necessarios para a administração do nosso usuario 
from django.contrib.auth.admin import UserAdmin
from .forms import ModelUsuarioCreateForm, ModelUsuarioChangeForm
from .models import ModelUsuario

from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe

@admin.register(ModelUsuario)  
class ModelUsuarioAdmin(UserAdmin):
    add_form=ModelUsuarioCreateForm  #o CreateForm passara a ser o formulario para adicionar novos usuarios 
    form= ModelUsuarioChangeForm #o ChargeForm servira para alteração dos usuarios 
    model=ModelUsuario
    list_display=('first_name', 'last_name', 'email', 'fone', 'is_staff','data_nascimento','sexo', 'cpf','endereco','curso', 'matricula', 'socio')
    actions = ['editar_registros']

    def edit_link(self, obj):
        change_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}">Editar</a>', change_url)

    edit_link.short_description = 'Editar'
    edit_link.allow_tags = True

    def editar_registros(self, request, queryset):
        if queryset.count() == 1:
            # Se apenas um registro for selecionado, redirecione para a página de edição desse registro
            obj = queryset.first()
            change_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
            return HttpResponseRedirect(change_url)
        else:
            # Se mais de um registro for selecionado, exiba uma mensagem informando que apenas um pode ser editado por vez
            self.message_user(request, "Você só pode editar um registro por vez.")

    editar_registros.short_description = "Editar registros selecionados"
    #quais dados apresentarao acessar a area administrativa? veja:
    fieldsets=(
        (None, {'fields':('email', 'password')}),
        ('Informações pessoais', {'fields':('first_name', 'last_name', 'fone', 'data_nascimento','sexo', 'cpf','endereco','curso', 'matricula', 'socio')} ),
        ('permissoes',{'fields':('is_active', 'is_staff')}),
    )




    