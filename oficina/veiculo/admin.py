from django.contrib import admin
from .models import Veiculo

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'cor', 'ano', 'placa', 'foto_veiculo')


admin.site.register(Veiculo, VeiculoAdmin)