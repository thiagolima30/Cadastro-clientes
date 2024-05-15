from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    
class OperacaoLog(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    operacao = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.operacao} - {self.timestamp}"