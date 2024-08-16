from django.db import models
from django.contrib.auth.models import User

class Docente (models.Model):
    matricula = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.matricula

class ServidorNapne(models.Model):
    cpf = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.cpf

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    matricula = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='fotos_alunos')
    def __str__(self):
        return self.nome

class PEI(models.Model):
    criacao = models.DateField('criação', auto_now_add=True, editable=False)
    modificacao = models.DateField('modificação', auto_now_add=True)
    operadores = models.ManyToManyField(ServidorNapne)
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)
    def __str__(self):
        return 'PEI do aluno ', self.aluno.nome

class SemestreLetivo(models.Model):
    ano = models.IntegerField()
    periodo = models.IntegerField('período')
    atual = models.BooleanField(default=True)
    pei = models.ForeignKey(PEI, on_delete=models.CASCADE)
    def __str__(self):
        return '{}.{} '.format(self.ano, self.periodo)










