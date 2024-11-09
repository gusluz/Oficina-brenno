from django.db import models
from cliente.models import Cliente

class Veiculo(models.Model):
    cliente_nome = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Nome do Cliente')
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    placa = models.CharField(max_length=8)
    foto_veiculo = models.ImageField(upload_to='images/', blank=True, verbose_name='Foto do veiculo')

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    def __str__(self):
        return self.modelo