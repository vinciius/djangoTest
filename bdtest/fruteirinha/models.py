from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Criando o modelo 'Fruta' para armazenar informações sobre as frutas cadastradas.
class Fruta(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
