import matplotlib
matplotlib.use('Agg')  # Define um backend sem interface gráfica
import matplotlib.pyplot as plt
import io
from io import BytesIO
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

    # Dados para o gráfico de barra
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

    # Contar a quantidade de vezes que cada produto foi utilizado
    produtos_usados = OS.objects.values('produtos_utilizados__nome').annotate(total=Count('produtos_utilizados')).order_by('-total')

    # Pegar os 3 produtos mais usados (ou menos, se não houver 3 disponíveis)
    top_produtos = list(produtos_usados[:3])

    # Verificar e ajustar listas
    if not top_produtos:
        labels = ['Nenhum produto encontrado']
        sizes = [1]  # Adiciona um valor padrão para evitar erro
    else:
        labels = [produto['produtos_utilizados__nome'] for produto in top_produtos]
        sizes = [produto['total'] for produto in top_produtos]

    # Garantir que labels e sizes têm o mesmo tamanho
    while len(labels) < len(sizes):
        sizes.pop()  # Remove o excesso
    while len(sizes) < len(labels):
        labels.pop()

    # Gerar o gráfico de barras
    plt.figure(figsize=(10, 5))  # Ajuste do tamanho
    bars = plt.bar(labels, sizes, color=['#ff9999', '#66b3ff', '#99ff99'])

    # Adicionar título e ajustes
    plt.title("Top 3 Produtos Utilizados", fontsize=14)
    plt.xlabel('Produtos', fontsize=12)
    plt.ylabel('Quantidade Utilizada', fontsize=12)

    # Ajuste do tamanho da fonte nos rótulos
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Salvar o gráfico como imagem
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')

    # Renderizar o template
    return render(
        request, 
        'dashboard.html', 
        {
            'produtos_proximos_minimo': produtos_proximos_minimo,
            'ordens_abertas': ordens_abertas,
            'grafico': image_base64,
            'chart': graphic
        }
    )
