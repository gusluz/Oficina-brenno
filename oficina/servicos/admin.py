from django.contrib import admin
from .models import Servico

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('cliente_nome', 'codigo', 'valor_custo', 'descricao')
    search_fields = ('cliente_nome', 'codigo')


admin.site.register(Servico, ServicoAdmin)