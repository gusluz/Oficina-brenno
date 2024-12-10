from django.shortcuts import render
from produto.models import Produto
from ordem_servico.models import OS
from datetime import datetime
from django.db.models import F

def dashboard_view(request):
    # Produtos próximos da quantidade mínima
    produtos_proximos_qtd_minima = Produto.objects.filter(qtd_atual__lte=F('qtd_minima') + 5)

    # Ordens realizadas no mês atual
    mes_atual = datetime.now().month
    ordens_mes = OS.objects.filter(data_inicio__month=mes_atual).count()

    # Contexto para o template
    context = {
        'produtos_proximos_qtd_minima': produtos_proximos_qtd_minima,
        'ordens_mes': ordens_mes,
    }
    return render(request, 'dashboard/dashboard.html', context)
    