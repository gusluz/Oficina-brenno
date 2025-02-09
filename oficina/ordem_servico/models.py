from django.db import models
from produto.models import Produto
from cliente.models import Cliente
from veiculo.models import Veiculo

class OS(models.Model):
    cliente_nome = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Nome do Cliente')
    veiculo = models.ManyToManyField(Veiculo, verbose_name='Veiculo do Cliente')
    foto_inicio = models.ImageField(upload_to='images/', blank=True, verbose_name='Foto do veiculo antes da OS')
    data_inicio = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name="Data de inicio")
    data_fim = models.DateTimeField(null=True, blank=True, verbose_name="Data de entrega")
    foto_fim = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Foto do veiculo depois da OS')
    codigo = models.CharField(max_length=100, unique=True)
    mao_obra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor da mão de obra')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField('OBSERVAÇÕES', blank=True)
    status = models.BooleanField(default=True, verbose_name='STATUS')

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'

    def __str__(self):
        return f'{self.cliente_nome} - {self.codigo}'


class OSProduto(models.Model):
    ordem_servico = models.ForeignKey(OS, on_delete=models.CASCADE, related_name='os_produtos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produto_os')
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade} unidades'
    