from django.contrib import admin
from .models import Produto


class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'qtd_atual', 'custo_final', 'fornecedor']


admin.site.register(Produto, ProdutoModelAdmin)
