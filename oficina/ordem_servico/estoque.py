from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import OSProduto, Produto


@receiver(post_save, sender=OSProduto)
def atualizar_estoque(sender, instance, created, **kwargs):
    if created:
        produto = instance.produto
        quantidade_usada = instance.quantidade

        with transaction.atomic():
            try:
                if quantidade_usada > produto.qtd_atual:
                    raise ValidationError(
                        "Quantidade solicitada maior que a disponível em estoque."
                    )

                produto.qtd_atual -= quantidade_usada
                if produto.qtd_atual < 0:
                    produto.qtd_atual = 0
                produto.save()
            except ValidationError as e:
                # Logar o erro ou enviar notificação
                print(f"Erro ao atualizar o estoque: {e}")
