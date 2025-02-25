from django.db import transaction
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import OSProduto, Produto


@receiver(pre_save, sender=OSProduto)
def verificar_estoque(sender, instance, **kwargs):
    produto = instance.produto
    quantidade_usada = instance.quantidade

    if quantidade_usada > produto.qtd_atual:
        raise ValidationError(
            "Quantidade solicitada maior que a disponível em estoque."
        )


@receiver(post_save, sender=OSProduto)
def atualizar_estoque(sender, instance, created, **kwargs):
    produto = instance.produto
    quantidade_usada = instance.quantidade

    with transaction.atomic():
        try:
            if created:
                produto.qtd_atual -= quantidade_usada
            else:
                # Recuperar a quantidade original do produto antes da atualização
                original_instance = OSProduto.objects.get(pk=instance.pk)
                quantidade_original = original_instance.quantidade
                produto.qtd_atual += quantidade_original - quantidade_usada

            if produto.qtd_atual < 0:
                produto.qtd_atual = 0
            produto.save()
        except ValidationError as e:
            # Logar o erro ou enviar notificação
            print(f"Erro ao atualizar o estoque: {e}")


@receiver(pre_delete, sender=OSProduto)
def restaurar_estoque(sender, instance, **kwargs):
    produto = instance.produto
    quantidade_usada = instance.quantidade

    with transaction.atomic():
        produto.qtd_atual += quantidade_usada
        produto.save()
