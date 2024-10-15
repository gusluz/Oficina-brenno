from django.contrib import admin
from .models import Cliente


class ClienteModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf_cnpj', 'telefone', 'criado_em']


admin.site.register(Cliente, ClienteModelAdmin)
