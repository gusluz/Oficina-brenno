from django.shortcuts import render
from produto.models import Produto
from ordem_servico.models import OS
from django.db.models import F
from django.db.models.functions import TruncMonth
from django.db.models import Count, functions
import calendar
from datetime import datetime

def dashboard(request):
    # Produtos próximos da quantidade mínima
    produtos_proximos_minimo = Produto.objects.filter(qtd_atual__lte=F('qtd_minima') + 2)

    # Ordens de Serviço abertas (data_entrega é None)
    ordens_abertas = OS.objects.filter(data_fim__isnull=True)
    #print("Ordens abertas:", ordens_abertas)  # Depuração, vai exibir as ordens abertas

    # Filtro de OS abertas
    os_abertas = OS.objects.filter(data_fim__isnull=True)

    # Consulta os meses em que há OS finalizadas
    ordens_finalizadas_por_mes = (
        OS.objects.filter(data_fim__isnull=False)
        .annotate(mes=functions.TruncMonth('data_fim'))
        .values('mes')
        .annotate(total=Count('id'))
        .order_by('mes')
    )
    #print("Ordens finalizadas:", ordens_finalizadas_por_mes)  # Depuração, vai exibir as ordens finalizadas


    # Lista fixa com todos os meses do ano atual
    meses_do_ano = {month: 0 for month in range(1, 13)}

    # Preenche os meses com os dados do banco
    for item in ordens_finalizadas_por_mes:
        mes = item['mes'].month  # Extrai o número do mês
        meses_do_ano[mes] = item['total']

    # Formata para o gráfico
    labels = [calendar.month_name[mes] for mes in meses_do_ano.keys()]
    data = list(meses_do_ano.values())

    return render(request, 'dashboard.html', {
        'produtos_proximos_minimo': produtos_proximos_minimo,
        'ordens_abertas': ordens_abertas,
        'os_abertas': os_abertas,
        'ordens_finalizadas_por_mes': ordens_finalizadas_por_mes,
        'labels': labels,  # Meses do ano
        'data': data,      # Quantidade de OS por mês
    })

# Exemplos de consultas
#from ordem_servico.models import OS
#OS.objects.filter(data_fim__isnull=True)  # Ordens abertas
#OS.objects.filter(data_fim__isnull=False)  # Ordens finalizadas