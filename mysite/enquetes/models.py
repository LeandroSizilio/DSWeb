from django.db import models

class Pergunta(models.Model):
    texto = models.CharField(max_length=150)
    data_pub = models.DateTimeField('Data de publicação')

class Alternativa(models.Model):
    texto = models.CharField(max_length=100)
    quant_votos = models.IntegerField('Quantidade de votos', default=0)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
