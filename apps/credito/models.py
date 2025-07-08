from django.db import models

# Create your models here.
class Credito(models.Model):
    acumulado = models.IntegerField("Acumulado")
    valor = models.IntegerField("Valor")