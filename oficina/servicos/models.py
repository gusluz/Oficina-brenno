from django.db import models
from produto.models import Produto
from cliente.models import Cliente

class Servico(models.Model):
    cliente_nome = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Nome do Cliente')
    codigo = models.CharField(max_length=100, unique=True)
    valor_custo = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True)
    produtos_utilizados = models.ManyToManyField(Produto, verbose_name='Produtos Utilizados')

    def __str__(self):
        return f'{self.cliente_nome} - {self.codigo}'
