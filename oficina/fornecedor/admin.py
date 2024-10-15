from django.contrib import admin
from .models import Fornecedor


class FornecedorModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf_cnpj', 'criado_em']


admin.site.register(Fornecedor, FornecedorModelAdmin)