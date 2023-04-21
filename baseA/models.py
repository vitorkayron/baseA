from django.db import models

# Create your models here.

class Cliente(models.Model):
    cpf = models.CharField(max_length=16, null=False, blank=False)
    nome = models.CharField(max_length=150, null=False)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField(null=True)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)
    lista_dividas = models.TextField()