from django.db import models
from cliente.validators import *
from cliente.estados_choices import *

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField('NOME', max_length=255)

    # criar validator CNPJ
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=18, validators=[validate_cpf_cnpj])

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
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'


    def __str__(self) -> str:
        return self.nome


    def save(self, *args, **kwargs):
        self.cpf_cnpj = validate_cpf_cnpj(self.cpf_cnpj)
        super(Fornecedor, self).save(*args, **kwargs)
