from django.db import models
from .validators import *
from .estados_choices import *

# Create your models here.
class Cliente(models.Model):
    
    nome = models.CharField('NOME', max_length=255)
    cpf_cnpj = models.CharField('CPF', max_length=18, validators=[validate_cpf_cnpj])
    data_nascimento = models.DateField('NASCIDO EM')
    telefone = models.CharField('TELEFONE 1', max_length=20, validators=[validate_phone])
    telefone2 = models.CharField('TELEFONE 2', max_length=20, validators=[validate_phone], blank=True)
    email = models.EmailField('EMAIL', blank=True)
    endereco_cep = models.CharField('CEP', max_length=10, blank=True)
    endereco_logradouro = models.CharField('ENDEREÇO', max_length=255, blank=True)
    endereco_numero = models.CharField('NÚMERO', max_length=10, blank=True)
    endereco_bairro = models.CharField('BAIRRO', max_length=255, blank=True)
    endereco_cidade = models.CharField('CIDADE', max_length=255, blank=True)
    endereco_estado = models.CharField('ESTADO', max_length=2, choices=ESTADOS_CHOICES, blank=True)
    endereco_complemento = models.CharField('COMPLEMENTO', max_length=255, blank=True)
    observacao = models.TextField('OBSERVAÇÕES', blank=True)
    criado_em = models.DateTimeField('CRIADO EM', auto_now_add=True)


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


    def __str__(self) -> str:
        return self.nome


    def save(self, *args, **kwargs):
        self.cpf_cnpj = validate_cpf_cnpj(self.cpf_cnpj)
        super(Cliente, self).save(*args, **kwargs)