from django.db import models
from django.utils import timezone

# Create your models here.

class Pergunta(models.Model):

    def __str__(self):
        return self.texto

    texto = models.CharField(max_length=300)
    data = models.DateTimeField(default=timezone.now)

class Alternativa(models.Model):

    def __str__(self):
        return self.texto

    pergunta = models.ForeignKey(Pergunta, models.CASCADE)
    texto = models.CharField(max_length=150)
    votos = models.IntegerField(default=0)