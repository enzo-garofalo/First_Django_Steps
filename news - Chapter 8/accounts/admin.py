from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    # Especifica o formulário que será usado para adicionar novos usuários na interface administrativa.
    # Aqui, é definido como CustomUserCreationForm, o que permite incluir campos adicionais (como age) na criação do usuário.
    
    form = CustomUserChangeForm
    # Especifica o formulário que será usado para editar ou atualizar usuários na interface administrativa.
    # Aqui, é definido como CustomUserChangeForm, o que mantém a consistência com os campos adicionais do modelo.
    
    model = CustomUser
    # Customizando os campos que vai estar presente na adm do django!
    # Verificar antes e depois do código em [Material]
    list_display = ['email', 'username', 'age', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields' :  ('age', )}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields' : ('age',)}),
    )

    # Estabeleci os campos que devem aparecer, e quais foram adicionados para aparecer no adm do django!


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)