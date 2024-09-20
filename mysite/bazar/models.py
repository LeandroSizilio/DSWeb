from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Cliente(models.Model):
    nome = models.CharField('Nome do cliente', max_length=100, null=False)

    login = models.CharField('Nome do usuário', max_length=100, null=False)

    senha = models.CharField('Senha', max_length=20, null=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cliente: {self.nome}"


class Evento(models.Model):
    id = models.BigAutoField(editable=False, primary_key=True)

    nome = models.CharField('Nome do evento', max_length=100, null=False)

    banner = models.ImageField('Banner', upload_to='fotos/', null=False)

    data_inicio = models.DateTimeField('Inicio do evento', null=False)

    data_fim = models.DateTimeField('Fim do evento',  null=True)
    
    def dataformatada(self):
        return f"De: {self.data_inicio.strftime('%d-%m')} até {self.data_fim.strftime('%d-%m')}"

    def __str__(self):
        return f"Evento: {self.nome} - Início: {self.data_inicio} - Fim: {self.data_fim}"


class Item(models.Model):
    id = models.BigAutoField(editable=False, primary_key=True)

    descricao = models.CharField('Descrição', null=False, max_length=60)

    preco = models.FloatField('Preço', validators=[MinValueValidator(0.0)], null=False)

    foto = models.ImageField('Imagem', upload_to='fotos/', null=False)

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default=None)

    reservado = models.BooleanField('Reservado', default=False)

    def __str__(self):
        return f"Item: {self.descricao} - Imagem: {self.foto} - Preço: {self.preco}"
