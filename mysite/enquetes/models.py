import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# fazer o migrate


# fazer o PerguntaAdmin no admin.py



class Autor(models.Model):
    descricao = models.CharField('Descricao', max_length=100)

    cidade = models.CharField('Cidade', max_length=40)

    pais = models.CharField('País', max_length=20)

    generos = models.TextField('Gêneros', blank=True, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {} {}".format(self.descricao, self.cidade, self.pais, self.generos, self.user)

    class Meta:
        verbose_name_plural = 'Autores'



class Rotulo(models.Model):
    titulo = models.CharField(max_length=25)

    def __str__(self):
        return "{}".format(self.titulo)

    class Meta:
        verbose_name_plural = 'Rótulo'


class Pergunta(models.Model):
    texto= models.CharField(max_length=200)

    data_pub = models.DateTimeField('Data de publicação')

    data_fim = models.DateField('Data de encerramento', default='2024-12-31', null=True)

    autor = models.ForeignKey(Autor, null=True, on_delete=models.CASCADE)

    rotulos = models.ManyToManyField(Rotulo)

    def publicada_recentemente(self):
        agora = timezone.now()

        return self.data_pub >= agora - datetime.timedelta(hours=24)


    def __str__(self):
        return "{} ({})".format(self.texto, self.id)


class Alternativa(models.Model):
    texto= models.CharField(max_length=250)

    quant_votos= models.IntegerField('Quantidade de votos', default=0)

    pergunta_associada= models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.texto, self.id)





