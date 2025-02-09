import matplotlib
matplotlib.use('Agg')  # Define um backend sem interface gráfica
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render
from django.db.models.functions import TruncMonth
from django.db.models import Count, functions
from produto.models import Produto
from ordem_servico.models import OS
from django.db.models import F
import calendar

def dashboard(request):
    # Produtos próximos da quantidade mínima
    produtos_proximos_minimo = Produto.objects.filter(qtd_atual__lte=F('qtd_minima') + 2)
    # Ordens de Serviço abertas
    ordens_abertas = OS.objects.filter(data_fim__isnull=True)
    
    # Quantidade de OS finalizadas por mês
    ordens_finalizadas_por_mes = (
        OS.objects.filter(data_fim__isnull=False)
        .annotate(mes=TruncMonth('data_fim'))
        .values('mes')
        .annotate(total=Count('id'))
        .order_by('mes')
    )

    # Dados para o gráfico
    meses_do_ano = {month: 0 for month in range(1, 13)}
    for item in ordens_finalizadas_por_mes:
        mes = item['mes'].month
        meses_do_ano[mes] = item['total']

    labels = [calendar.month_name[mes] for mes in meses_do_ano.keys()]
    data = list(meses_do_ano.values())

    # Gerar o gráfico com Matplotlib
    plt.figure(figsize=(10, 5))
    plt.bar(labels, data, color='skyblue')
    plt.title("OS Realizadas por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Salvar o gráfico em memória
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Renderizar o template
    return render(
        request, 
        'dashboard.html', 
        {
            'produtos_proximos_minimo': produtos_proximos_minimo,
            'ordens_abertas': ordens_abertas,
            'grafico': image_base64,
        }
    )
