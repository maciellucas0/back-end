from django.db import models

# Create your models here.


class ModelDoArquivo(models.Model):
    nome_loja = models.CharField(max_length=26)
    valor = models.CharField(max_length=26)
    data = models.CharField(max_length=26)
    tipo = models.CharField(max_length=26)
    cartao = models.CharField(max_length=26)
    hora = models.CharField(max_length=9)
    dono = models.CharField(max_length=30)
    CPF = models.CharField(max_length=14)
