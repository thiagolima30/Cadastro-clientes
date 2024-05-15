# clientes/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Cliente, OperacaoLog

@receiver(post_save, sender=Cliente)
def log_cliente_save(sender, instance, created, **kwargs):
    if created:
        OperacaoLog.objects.create(usuario=instance.criado_por, operacao='Cliente criado')
    else:
        OperacaoLog.objects.create(usuario=instance.criado_por, operacao='Cliente atualizado')

@receiver(post_delete, sender=Cliente)
def log_cliente_delete(sender, instance, **kwargs):
    OperacaoLog.objects.create(usuario=instance.criado_por, operacao='Cliente excluído')
