from django.contrib import admin
from .models import OS

class OSAdmin(admin.ModelAdmin):
    list_display = ('cliente_nome', 'data_inicio', 'data_fim', 'mao_obra', 'descricao', 'valor_total', 'observacao')
    search_fields = ('cliente_nome', 'id')
    


admin.site.register(OS, OSAdmin)