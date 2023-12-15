from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from usuarios.forms import CustomUsuarioChangeForm, CustomUsuarioCreateForm
from usuarios.models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'telefone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informaçõs pessoais', {'fields': ('first_name', 'last_name', 'telefone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')})
    )