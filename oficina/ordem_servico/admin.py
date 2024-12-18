from django.contrib import admin
from .models import OS

class OSAdmin(admin.ModelAdmin):
    list_display = ('cliente_nome', 'data_inicio', 'data_fim', 'codigo', 'mao_obra', 'descricao', 'valor_total', 'observacao')
    search_fields = ('cliente_nome', 'codigo')
    


admin.site.register(OS, OSAdmin)