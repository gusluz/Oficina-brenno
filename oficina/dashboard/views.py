import matplotlib
matplotlib.use('Agg') # Define um backend sem interface gráfica
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum
from produto.models import Produto
from ordem_servico.models import OS, OSProduto
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
    
    # Dados para o gráfico de OS finalizadas por mês
    meses_do_ano = {month: 0 for month in range(1, 13)}
    for item in ordens_finalizadas_por_mes:
        mes = item['mes'].month
        meses_do_ano[mes] = item['total']
    labels_os = [calendar.month_name[mes] for mes in meses_do_ano.keys()]
    data_os = list(meses_do_ano.values())
    
    # Gerar o gráfico de OS finalizadas por mês
    plt.figure(figsize=(10, 5))
    plt.bar(labels_os, data_os, color='navy')
    plt.title("OS Realizadas por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.yticks(range(0, max(data_os) + 1))
    plt.tight_layout()
    
    # Salvar o gráfico em memória
    buffer_os = io.BytesIO()
    plt.savefig(buffer_os, format='png')
    buffer_os.seek(0)
    image_base64_os = base64.b64encode(buffer_os.read()).decode('utf-8')
    buffer_os.close()
    
    # Obtendo os 5 produtos mais utilizados
    produtos_mais_utilizados = (
        OSProduto.objects.values('produto__nome')
        .annotate(total_quantidade=Sum('quantidade'))
        .order_by('-total_quantidade')[:5]
    )
    
    # Extraindo os nomes dos produtos e as quantidades
    nomes_produtos = [produto['produto__nome'] for produto in produtos_mais_utilizados]
    quantidades = [produto['total_quantidade'] for produto in produtos_mais_utilizados]
    
    # Gerar o gráfico dos 5 produtos mais utilizados
    plt.figure(figsize=(10, 5))
    plt.bar(nomes_produtos, quantidades, color=['blue', 'orange', 'green'])
    plt.title("Top 5 Produtos Mais Utilizados")
    plt.xlabel("Produtos")
    plt.ylabel("Quantidade Utilizada")
    plt.yticks(range(0, max(quantidades) + 1))
    plt.tight_layout()
    
    # Salvar o gráfico em memória
    buffer_produtos = io.BytesIO()
    plt.savefig(buffer_produtos, format='png')
    buffer_produtos.seek(0)
    image_base64_produtos = base64.b64encode(buffer_produtos.read()).decode('utf-8')
    buffer_produtos.close()
    
    # Renderizar o template
    return render(request, 'dashboard.html', {
        'produtos_proximos_minimo': produtos_proximos_minimo,
        'ordens_abertas': ordens_abertas,
        'grafico_os': image_base64_os,
        'grafico_produtos': image_base64_produtos,
    })
