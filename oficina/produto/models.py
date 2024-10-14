from django.db import models

from fornecedor.models import Fornecedor


class Produto(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, verbose_name='Fornecedor')
    codigo = models.CharField(max_length=100, unique=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    outras_despesas = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    custo_final = models.DecimalField(max_digits=10, decimal_places=2)
    lucro = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_minima = models.IntegerField()
    qtd_maxima = models.IntegerField()
    qtd_atual = models.IntegerField()

    def __str__(self):
        return self.nome